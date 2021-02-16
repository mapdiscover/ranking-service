# Mastering Ranking Database for MapDiscover Ranking Service

## How to use this guide

All command are to be executed inside the `rdb` database.

## SQL Queries

### Operations on table `public.global`

#### Manual add of an entry to the said table e.g.

```sql
insert into global 
(identifier,bbox, "00:00-04:00","04:00-08:00","08:00-12:00","12:00-16:00","16:00-20:00", "20:00-00:00")
values
(765770, ST_SetSRID(ST_MAKEPOINT(10.6554, 53.9403), 4326), 0, 0, 0, 0, 0, 0);
```

#### Get the results the service works with including data about the region the POI is in:

```sql
select * from (select * from global where identifier={0}) as g
inner join poiregion on poiregion.identifier = g.identifier;
```
