#!/usr/bin/python3
import os
_DEEPLEVELS = 5
data = {}
ranking = {}
listSorted = []
def getFile():
	global data
	sfile = open("poiclicks.txt", "r")
	filebuffer = sfile.read()
	sfile.close()
	for entry in filebuffer.split("\n"):
		if entry.find(" ") > -1:
			click, pois = entry.split(" ", 1)
		else:
			click, pois = (entry, "")
		if click in data:
			data[click] += pois
		else:
			data[click] = pois
def createList():
	global data, listSorted
	for entry in data:
		if not entry == "":
			listSorted.append(int(entry))
	listSorted.sort()
	#listSorted.reverse()
def createRanking():
	global listSorted, _DEEPLEVELS, ranking
	order = []
	length = len(listSorted)
	step = length / _DEEPLEVELS
	step = round(step) -1
	if step <= 0:
		step = 1
	start = 0
	stop = step
	for i in range(0, _DEEPLEVELS):
		order.append(i)
	order.reverse()
	for i in order:
		ranking[i] = listSorted[start : stop]
		if len(ranking[i]) == 0:
			ranking[i].extend(ranking[i+1])
		start = stop
		stop += step
	sfile = open("rankingFinish.json", "w")
	sfile.write(str(ranking))
	sfile.close()
def layering():
	global ranking, _DEEPLEVELS
	output = {}
	index = _DEEPLEVELS
	ranking[len(ranking)-1].append(0)
	for rank in ranking:
		output[rank] = ""
		clickList = ranking[rank]
		clickList.sort()
		output[rank] = str(clickList[0])
		if rank-1 in ranking:
			clickList2 = ranking[rank-1]
			clickList2.sort()
			output[rank] += "-" + str(clickList2[0])
		else:
			output[rank] += "-<infinity>"
		index += 1
	sfile = open("layerFinish.json", "w")
	sfile.write(str(output))
	sfile.close()
def main():
	getFile()
	createList()
	createRanking()
	layering()
main()
