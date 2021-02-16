# Adding data to RDB

**We decided against using this strategy and therefore against using OSM data for 'rastering regions' because with this we get unorthogonal results. The new solution works with data from EUROSTAT and for preparing and importing data QGIS and a different import strategy as well!**

## How to populate Database

You import with

```bash
osm2pgsql --style source.txt --create --latlong --database rdb --multi-geometry schleswig-holstein-latest.osm.pbf
```

- **--style source.txt**: The file `source.txt` specifies the table schema to use.

- **--create**: Rewrite the database. Use `--append` to add to existing database

- **--latlong**: Optimisation for analysis.

- **--database regions**: The name of the database to import to e.g. `regions`
  
  - Additionally pass also the `--password` to be prompted for database password.

- **--multi-geometry**: Used for analysis. It summarizes the geometries of polygons relating to each other in one object to one multipolygon object.

- **schleswig-holstein-latest.osm.pbf**: The pbf to read from.

## How to make the Database minimal

osm2pgsl imports many irrelevant stuff we do not need. In order to filter out what we really want, we need to connect to the `rdb` DB and issue the following commands.

### First creating the target table

We use the target table to put what we want inside and to delete everything around it. If it does not exist then we need to create it by using the following query:

```sql
CREATE TABLE regions (name text, bbox geometry);
```

### Putting inside what we want

```sql
INSERT INTO regions SELECT name, way FROM planet_osm_polygon WHERE boundary='administrative' AND admin_level='6' AND name IS NOT NULL;
```

### Clean up table (remove overlapping boundaries)

```sql
DELETE FROM regions where (SELECT * FROM regions a, regions b WHERE ST_Contains(a.geom, b.geom));
```

### Deleting everything else

```sql
DROP TABLE planet_osm_polygon;
DROP TABLE planet_osm_line;
DROP TABLE planet_osm_point;
DROP TABLE planet_osm_roads;
```
