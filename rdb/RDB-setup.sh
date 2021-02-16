#!/usr/bin/bash
# Please run this group as the database superuser and not as operating system's root
# This set ups the Ranking Database (R-DB) in Postgres automatically inclusive the activation of extensions. After this script has run you have a fully functional R-DB database for MapDiscover Ranking Service.
psql -c "CREATE DATABASE rdb;"
psql -d rdb -c "CREATE EXTENSION postgis;"
psql -d rdb -c "CREATE TABLE global (identifier uuid, region text, bbox geometry, trangea int,trangeb int,trangec int,tranged int,trangee int,trangef int);"
psql -d rdb -c "CREATE TABLE regions (id text, name text, bbox geometry);"
