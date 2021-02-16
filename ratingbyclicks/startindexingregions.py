#!/usr/bin/env python3
import utils, threading, sys, copy, os, json
#_threads = 5
#_levelsOfRanking = 5 #Original value: '5'. For debugging changed to '1'
#_tableRegions = "regions"
_singleregion = False
#_dbconnstr = "dbname=rdb"
class ranking():
	def removeDoubles(self, clickList):
		for entry in clickList:
			self.data[entry] = True
	
	def createList(self):
		for entry in self.data:
			if not entry == "":
				self.listSorted.append(int(entry))
		self.listSorted.sort()
		#self.listSorted.reverse()
	
	def createRanking(self):
		order = []
		length = len(self.listSorted)
		step = length / self._DEEPLEVELS
		step = round(step) -1
		if step <= 0:
			step = 1
		start = 0
		stop = step
		for i in range(0, self._DEEPLEVELS):
			order.append(i)
		order.reverse()
		for i in order:
			self.ranking[i] = self.listSorted[start : stop]
			if len(self.ranking[i]) == 0:
				self.ranking[i].extend(self.ranking[i+1])
			start = stop
			stop += step
	
	def layering(self, filename):
		output = {}
		index = self._DEEPLEVELS
		self.ranking[len(self.ranking)-1].append(0)
		for rank in self.ranking:
			output[rank] = ""
			clickList = self.ranking[rank]
			clickList.sort()
			output[rank] = str(clickList[0])
			if rank-1 in self.ranking:
				clickList2 = self.ranking[rank-1]
				clickList2.sort()
				output[rank] += "-" + str(clickList2[0])
			else:
				output[rank] += "-<infinity>"
			index += 1
		sfile = open(os.path.join("regions", filename + ".json"), "w")
		sfile.write(json.dumps(output))
		sfile.close()
	def __init__(self, clickList, filename):
		self._DEEPLEVELS = _levelsOfRanking
		self.data = {}
		self.ranking = {}
		self.listSorted = []
	
		self.removeDoubles(clickList)
		self.createList()
		self.createRanking()
		self.layering(filename)

class regions(utils.utils, utils.dbActions):
	def __init__(self):
		self.regionCur, self.regionConn = self._establishConnToDB(_dbconnstr)
		self.regionCur.execute(self.getregions()["query"])
	def endFetching(self):
		self._closeConnToDB(self.regionCur, self.regionConn)
	def fetchNextRegion(self):
		region = self.regionCur.fetchone()
		if region == None:
			self.endFetching()
			return False
		return region[0]

class fetchandcoordinate(utils.utils, utils.dbActions, utils.columnSchemes):
	def toClickList(self, row):
		clicks = []
		tablecolumn = self.getentry()["columns"]
		prefix = self.rankingdataprefix
		if row == None:
			return []
		index = 0
		for cell in row:
			if tablecolumn[index].startswith(prefix):
				clicks.append(int(cell))
			index += 1
		return clicks
	def __init__(self, nextRegion):
		self.getSchemes()
		clicks = []
		clicksCur, clicksConn = self._establishConnToDB(_dbconnstr)
		print("Fetching clicks for region '" + str(nextRegion) + "'")
		clicksCur.execute(self.rankingdatabyregion()["query"].replace("{0}", str(nextRegion)))
		row = "init"
		while not row == None:
			row = clicksCur.fetchone()
			clicks.extend(self.toClickList(row))
		self._closeConnToDB(clicksCur, clicksConn)
		if len(clicks) >= _levelsOfRanking*3:
			ranking(clicks, nextRegion)
		else:
			print("  not enough clicks for region '" + str(nextRegion) + "'")

class prepareForRankingAlgo(regions):
	def start(self):
		loop = True
		while loop:
			while _threads >= threading.activeCount():
				if not _singleregion:
					nextRegion = self.fetchNextRegion()
				else:
					nextRegion = _singleregion
				if nextRegion != False:
					x = threading.Thread(target=fetchandcoordinate, args=(copy.deepcopy(nextRegion),))
					x.start()
					if _singleregion:
						return 0
				else:
					return 0

def main():
	global _threads, _singleregion
	args = sys.argv
	del args[0]
	for i in range(0, len(args)):
		if args[i] == "-n" or args[i] == "--threads":
			_threads = int(args[i+1])
		elif args[i] == "-r" or args[i] == "--region":
			_singleregion = args[i+1]
			_threads = 1
	prepareForRankingAlgo().start()

if __name__ == "__main__":
	main()
