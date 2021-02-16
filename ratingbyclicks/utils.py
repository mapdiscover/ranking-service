#!/usr/bin/env python3
import psycopg2
class columnSchemes():
	def getSchemes(self):
		self.table_global = ["identifier", "region", "bbox", "trangea", "trangeb", "trangec", "tranged", "trangee", "trangef"]
		self.trangeMatch = {"trangea": "00:00-04:00", "trangeb": "04:00-08:00", "trangec": "08:00-12:00", "tranged": "12:00-16:00", "trangee": "16:00-20:00", "trangef": "20:00-00:00"}
		self.rankingdataprefix = "trange"
		return self
class dbActions(columnSchemes):
	def getentry(self):
		self.getSchemes()
		return {"columns": self.table_global, "query": "select * from global where identifier='{0}'"} # Don't add a ';' behind the query because this would then break the ' UNION ALL ' statement
	def increaseclick(self):
		return {"query": "update global set {0} = {0} +{1} where identifier='{2}';"}
	def deleteentry(self):
		return {"query": "DELETE FROM global WHERE identifier='{0}';"}
	def createentry(self):
		self.getSchemes()
		return {"query": "INSERT INTO global (" + ", ".join(self.table_global) + ") VALUES ({0});"}
	def getregions(self):
		return {"query": "select id from regions;"}
	def rankingdatabyregion(self):
		return {"query": "select * from global where region='{0}';"}
class utils():
	def _establishConnToDB(self, dbconnstr):
		#connect to database
		conn = psycopg2.connect(dbconnstr)
		cur = conn.cursor()
		return cur, conn
	
	def _closeConnToDB(self, cur, conn):
		#close connection to database
		cur.close()
		conn.close()
	
	def _sendToDB(self, query, dbconnstr):
		#connect to database, send query and fetch result, close connection (simple version)
		cur, conn = self._establishConnToDB(dbconnstr)
		cur.execute(query)
		conn.commit()
		print(query)
		try:
			result = cur.fetchall()
		except:
			result = None
		self._closeConnToDB(cur, conn)
		return result
