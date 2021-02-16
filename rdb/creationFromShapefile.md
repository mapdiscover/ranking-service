This is a specification for a database that contains the region data used for the ranking.

# How to create Database

In a terminal execute the following to create the DB in Postgres via `psq` command. See also file `regions-setup.sh` included within this document.

# Add region data to RDB

## How to populate Database

1. You import from within QGIS in a table called `regionstmp`

Many unrelevant stuff we do not need gets imported . In order to filter out what we really want, we need to connect to the `rdb` DB and issue the following commands.

### Putting inside what we want (we created the table 'regions' beforehand by executing the script)

```sql
INSERT INTO regions SELECT gisco_id, lau_label, geom FROM regionstmp;
```

### Deleting import table

```sql
DROP TABLE regionstmp;
```

## As batch

```sql
INSERT INTO regions SELECT gisco_id, lau_label, geom FROM regionstmp;
DROP TABLE public.regionstmp;
```
