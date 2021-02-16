#!/usr/bin/env python3
from concurrent import futures
from lib import database
from lib import dbsetup

import time, utils, math, os, sys, grpc, yaml, logging
import mdrankingservice_pb2 as pb2
import mdrankingservice_pb2_grpc as pb2_grpc
import json as jsonLib

dbhelper = None
config = {}
regionRanking = {}
#events = {"mapclick": 1, "searchresultclick": 2} #the numbers represent the increase ( e.g. '+1' ) for a specified event
#_dbconnstr = "dbname=rdb"
_SQLCONNECT = " UNION ALL "
#columnScheme = utils.columnSchemes().getSchemes()

class ratingService(pb2_grpc.MDRankingServiceServicer):
	"""def _toJSON(self, table, columns):
		data = {}
		for row in table:
			col = {}
			ident = ""
			for i in range(0, len(columns)):
				if columns[i] == "identifier":
					ident = row[i]
				col[columns[i]] = row[i]
			data[ident] = col
		return data"""
	
	def _getRightColumn(self): # Done
		columnList = []
		invert_columnDict = {}
		for i in config["ranking_datacolumntimematch"]:
			columnList.append(config["ranking_datacolumntimematch"][i])
		for i in config["ranking_datacolumntimematch"]:
			invert_columnDict[config["ranking_datacolumntimematch"][i]] = i
		for trange in columnList:
			start, end = trange.split("-")
			pattern = "%Y-%m-%d %H:%M"
			ltime = time.localtime()
			startTime = str(ltime[0]) + "-" + str(ltime[1]) + "-" + str(ltime[2]) + " " + start
			if end == "00:00":
				endTime = str(ltime[0]) + "-" + str(ltime[1]) + "-" + str(ltime[2]) + " " + end
			else:
				endTime = str(ltime[0]) + "-" + str(ltime[1]) + "-" + str(ltime[2]+1) + " " + end
			start = int(time.mktime(time.strptime(startTime, pattern)))
			end = int(time.mktime(time.strptime(endTime, pattern)))
			if start <= time.time() < end:
				return invert_columnDict[trange]
		print("oink")
	def _increaseClick(self, identifier, event="mapclick"): # Done
		#query = self.increaseclick()["query"]
		query = config["increaseclick"]
		
		#find the column matching the current hour
		colname = self._getRightColumn()
		print(colname)
		
		#get the increment for event 'event'
		increment = config["ranking_weight"][event]
		
		#create query
		#query = query.replace("{0}", colname).replace("{1}", str(int(increment))).replace("{2}", str(identifier))
		query = dbhelper.modifyQuery(query, (int(increment), str(identifier)), [colname, colname])
		
		#return query
		return query
	"""def _preventHack(self, inp):
		for i in ["--", "/*", "*/", ";", "//"]:
			inp = inp.replace(i, "")
		return inp"""
	def _createDBEntry(self, identifier, bbox, send=True): # Done
		#query = self.createentry()["query"]
		#query = config["createentry"]
		#bbox = str(bbox[0])) + "," + self._preventHack(str(bbox[1]))
		#content = columnScheme.table_global
		
		#prepare the row to add
		#content[0] = "'" + self._preventHack(identifier) + "'"
		
		#prepare the coordinates
		#content[2] = "st_setsrid(st_makepoint(" + bbox + "), 4326)"
		
		#add 'region'
		#content[1] = "(select id from regions where st_dwithin(" + content[2] + ", regions.bbox, 0) limit 1)"
		
		#create the row, add '0' to the time ranges e.g. `0:00-04:00` and `04:00-8:00` to initiate the row
		#for i in range(3, len(content)):
		#	content[i] = "0"
		
		#build the query
		#query = query.replace("{0}", ",".join(content))
		query = dbhelper.modifyQuery(config["createentry"], (str(identifier), bbox[0], bbox[1], bbox[0], bbox[1]))
		
		#finally send it
		if send:
			#result = self._sendToDB(query, _dbconnstr)
			dbhelper.sendQuery(query, ())
		else:
			return query
	
	def getIdents(self, entry, context): # Partially done
		output = []
		identifiers = entry.identifiers.split(";")
		
		#create query
		query = []
		for ident in identifiers:
			#query.append(self.getentry()["query"].replace("{0}", str(self._preventHack(ident))))
			query.append(dbhelper.modifyQuery(config["getentry"], (str(ident),)))
		query = _SQLCONNECT.join(query) + ";"
		#send query to DB, fetch results and convert them to json
		#json = self._toJSON(self._sendToDB(query, _dbconnstr), self.getentry()["columns"])
		json = dbhelper.sendQuery(query, ()).get()
		
		#find the column matching the current hour
		colname = self._getRightColumn()
		
		#Translate the zoom information into ranking
		rank = str(int(entry.curzoom) - int(entry.minzoom))
		
		#just add the identifiers (each 'ident') matching their clicks in the current rank requested.
		for ident in json:
			sfile = open(os.path.join("regions", str(json[ident]["region"]) + ".json"), "r")
			index = jsonLib.loads(sfile.read())
			sfile.close()
			start, end = index[rank].split("-")
			if end == "<infinity>":
				end = math.inf
			if int(start) <= int(json[ident][colname]) < end:
				output.append(str(ident))
		
		#yield result as semicolon seperated list
		return pb2.identifiersOut(identifiersOut=";".join(output))
	
	def increaseClick(self, click, context): # Done
		#self._sendToDB(self._increaseClick(click.identifier, click.event), _dbconnstr)
		dbhelper.sendQuery(self._increaseClick(click.identifier, click.event), ()).get()
		return pb2.status(status="OK")
	
	def addEntry(self, entry, context): # Done
		output = "OK"
		#query = self.getentry()["query"]
		query = config["getentry"]
		
		#FIRST PART: Check for existence of the entry
		#  create query
		#query = query.replace("{0}", str(self._preventHack(entry.identifier)))
		#  ask DB for existence of the entry 'identifier'
		#json = self._toJSON(self._sendToDB(query, _dbconnstr), self.getentry()["columns"])
		json = dbhelper.sendQuery(query, (entry.identifier,)).get()
		
		# check, if the result contains any content
		if len(json) == 0:
			self._createDBEntry(entry.identifier, [entry.longitude, entry.latitude])
			return pb2.status(status=output)
		else:
			return pb2.status(status="Already exists in database")
	def feedback(self, status, context): # Done
		return pb2.status(status=status.status)
	def batch(self, diff, context): # Done
		output = "OK"
		diff = diff.diff
		""" Format of 'diff':
		{"added": [[identifier, [longitude, latitude]],...],
		"removed: [identifier, ...]"}
		"""
		query = []
		
		# Convert string JSON 'diff' to a dictionary
		diff = jsonLib.loads(diff)
		
		# Building a query for each entry to be added
		if "added" in diff:
			for obj in diff["added"]:
				if len(dbhelper.sendQuery(config["getentry"], (obj[0],), limit=1)) == 0:
					query.append(self._createDBEntry(obj[0], obj[1], send=False))
		
		# Building a query for each entry to be removed
		if "removed" in diff:
			for obj in diff["removed"]:
				query.append(self.deleteEntry(obj, obj, send=False))
		
		# Create batch query and send it
		#result = self._sendToDB("\n".join(query), _dbconnstr)
		dbhelper.sendQuery("\n".join(query), ()).get()
		return pb2.status(status=output)
	def deleteEntry(self, identifier, context, send=True): # Done
		output = "OK"
		#query = self.deleteentry()["query"]
		query = config["deleteentry"]
		
		#create query
		if type(identifier) is str:
			#query = query.replace("{0}", str(self._preventHack(identifier)))
			query = dbhelper.modifyQuery(query, (identifier,))
		else:
			#query = query.replace("{0}", str(self._preventHack(identifier.identifier)))
			query = dbhelper.modifyQuery(query, (identifier.identifier,))
		
		#send query
		if send:
			#result = self._sendToDB(query, _dbconnstr)
			result = dbhelper.sendQuery(query, ()).get()
			return pb2.status(status=output)
		else:
			return query


if __name__ == "__main__":
	logging.info("loading 'config.yml'...")
	sfile = open("config.yml", "r")
	config = yaml.safe_load(sfile)
	sfile.read()
	
	"""
	Environment variable: 'dbconnstr'
	Format of the env var according to https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
	"""
	
	if "environment" in config:
		logging.info("Setting environment variables from configuration...")
		for key in config["environment"]:
			logging.debug("Setting environment variable '{}' to value '{}'".format(key, config["environment"][key]))
			config[key] = config["environment"][key]
	
	if "dbconnstr" in os.environ:
		logging.info("Overwriting 'dbconnstr' from configuration...")
		config["dbconnstr"] = os.environ("dbconnstr")
	
	logging.info("perform automatic set up...")
	dbsetup.setupDB(config)
	logging.info("automatic set up performed!")
	
	logging.info("connecting to database...")
	dbhelper = database.helper(config)
	
	logging.info("Configuring GRPC server...")
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=config["gprc_workers"]))
	pb2_grpc.add_MDRankingServiceServicer_to_server(ratingService(), server)
	server.add_insecure_port('[::]:50051')
	
	logging.info("Starting server...")
	server.start()
	server.wait_for_termination()
	
	logging.info("shutdown event received!")
	logging.info("Disconnecting from database...")
	dbhelper.tearDown()
	
	logging.info("Bye, see you soon :)")
