#!/usr/bin/env python3
import grpc, json, os
import mdrankingservice_pb2 as pb2
import mdrankingservice_pb2_grpc as pb2_grpc

class debug():
	def test(self):
		print(self.addEntry("40e6215d-b5c6-4896-987c-f30f3678f608", 9.98363, 53.79518))
	def debug(self):
		diff = {"added": [["6ecd8c99-4036-403d-bf84-cf8400f67836", [9.97772, 53.79232]], ["3f333df6-90a4-4fda-8dd3-9485d27cee36", [9.43523, 54.78313]], ["3f444df6-90a4-4fda-8dd3-9485d27cee36", [9.43769, 54.78315]], ["3f444df6-90a4-4fda-8dd3-9485d27dff36", [9.43769, 54.78365]], ["40e6415d-b5c6-4895-987d-f30f3678f608", [10.68277, 53.86559]]], "removed": ["40e6215d-b5c6-4896-987c-f30f3678f608"]}
		self.addEntry("40e6215d-b5c6-4896-987c-f30f3678f608", 9.98363, 53.79518)
		self.batch(json.dumps(diff))
		for i in range(0, 10):
			self.increaseClick("6ecd8c99-4036-403d-bf84-cf8400f67836", "mapclick")
			self.increaseClick("3f333df6-90a4-4fda-8dd3-9485d27cee36", "mapclick")
			self.increaseClick("3f333df6-90a4-4fda-8dd3-9485d27cee36", "searchresultclick")
		for i in range(0, 4):
			self.increaseClick("3f444df6-90a4-4fda-8dd3-9485d27cee36", "searchresultclick")
		for i in range(0, 7):
			self.increaseClick("3f444df6-90a4-4fda-8dd3-9485d27dff36", "searchresultclick")
		for i in range(0, 10):
			self.increaseClick("40e6415d-b5c6-4895-987d-f30f3678f608", "mapclick")
		if "test" == self.feedback("test"):
			print("echo successful")
		os.system("python3 startindexingregions.py --threads 1 --region DE_01060039")
		os.system("python3 startindexingregions.py --threads 1 --region DE_01001000")
		os.system("python3 startindexingregions.py --threads 1 --region DE_01003000")
		result = self.getIdents("6ecd8c99-4036-403d-bf84-cf8400f67836;3f333df6-90a4-4fda-8dd3-9485d27cee36", 17, 17)
		self.deleteEntry("3f444df6-90a4-4fda-8dd3-9485d27dff36")
	def getIdents(self, identifiers, curzoom, minzoom=17):
		with grpc.insecure_channel("localhost:50051") as channel:
			stub = pb2_grpc.MDRankingServiceStub(channel)
			resp = stub.getIdents(pb2.identifiers(identifiers=identifiers, curzoom=curzoom, minzoom=minzoom))
			output = resp.identifiersOut
		return output
	def addEntry(self, identifier, long, lat):
		with grpc.insecure_channel("localhost:50051") as channel:
			stub = pb2_grpc.MDRankingServiceStub(channel)
			resp = stub.addEntry(pb2.entry(identifier=identifier, longitude=int(long), latitude=int(lat)))
			output = resp.status
		return output
	def increaseClick(self, identifier, event="mapclick"):
		with grpc.insecure_channel("localhost:50051") as channel:
			stub = pb2_grpc.MDRankingServiceStub(channel)
			resp = stub.increaseClick(pb2.click(identifier=identifier, event=event))
			output = resp.status
		return output
	def feedback(self, data):
		with grpc.insecure_channel("localhost:50051") as channel:
			stub = pb2_grpc.MDRankingServiceStub(channel)
			resp = stub.feedback(pb2.status(status=data))
			output = resp.status
		return output
	def batch(self, diff):
		with grpc.insecure_channel("localhost:50051") as channel:
			stub = pb2_grpc.MDRankingServiceStub(channel)
			resp = stub.batch(pb2.diff(diff=diff))
			output = resp.status
		return output
	def deleteEntry(self, identifier):
		with grpc.insecure_channel("localhost:50051") as channel:
			stub = pb2_grpc.MDRankingServiceStub(channel)
			resp = stub.deleteEntry(pb2.identifier(identifier=identifier))
			output = resp.status
		return output

if __name__ == "__main__":
	debug().debug()
