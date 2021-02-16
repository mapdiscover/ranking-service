#!/usr/bin/env python3
import requests
r = requests.post("http://127.0.0.1:8080/", data={"identifiers": "765850;765851", "curzoom": "17"})
print(r.request.body)
print(r.text)
if r.text == "765850":
	print(r.headers)
	print("First test working")

#r = requests.put("http://127.0.0.1:8080/", data={"identifier": "765850", })

"""
Running "CREATE DATABASE" and similiar SQL's of that kind:
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import psycopg2
conn = psycopg2.connect(_dbconnstr)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
cur.execute("CREATE DATABASE testdb;")
"""

""" Add to Database table 'global'
INSERT INTO public."global" (identifier, bbox, trangea, trangeb, trangec, tranged, trangee, trangef) VALUES(765854, 'POINT (9.98363 53.79518)', 0, 33, 12, 76, 10, 2);
INSERT INTO public."global" (identifier, bbox, trangea, trangeb, trangec, tranged, trangee, trangef) VALUES(765855, 'POINT (9.97772 53.79232)', 2, 22, 35, 32, 11, 4);
INSERT INTO public."global" (identifier, bbox, trangea, trangeb, trangec, tranged, trangee, trangef) VALUES(765856, 'POINT (9.43523 54.78313)', 4, 7, 12, 11, 5, 4);
INSERT INTO public."global" (identifier, bbox, trangea, trangeb, trangec, tranged, trangee, trangef) VALUES(765857, 'POINT (9.43769 54.78315)', 6, 6, 4, 3, 21, 5);
INSERT INTO public."global" (identifier, bbox, trangea, trangeb, trangec, tranged, trangee, trangef) VALUES(765858, 'POINT (9.43508 54.78365)', 16, 3, 2, 5, 2, 23);
INSERT INTO public."global" (identifier, bbox, trangea, trangeb, trangec, tranged, trangee, trangef) VALUES(765850, 'POINT (10.68277 53.86586)', 4, 15, 11, 4, 27, 4);
INSERT INTO public."global" (identifier, bbox, trangea, trangeb, trangec, tranged, trangee, trangef) VALUES(765852, 'POINT (10.68163 53.86559)', 10, 8, 0, 0, 0, 15);

INSERT INTO public."global" (identifier, bbox, trangea, trangeb, trangec, tranged, trangee, trangef) VALUES(765853, 'POINT (9.98403 53.79468)', 0, 23, 9, 23, 12, 2);
INSERT INTO public."global" (identifier, bbox, trangea, trangeb, trangec, tranged, trangee, trangef) VALUES(765851, 'POINT (10.68284 53.86607)', 1, 14, 9, 4, 30, 0);

"""
