# Rastering regions

**We decided against using this strategy and therefore against using OSM data for 'rastering regions' because with this we get unorthogonal results. The new solution works with data from EUROSTAT and for preparing and importing data QGIS.**

# Deprecated section

## Definitions

**Regions:** A piece of land (area) where all to OSM known objects can be put in relacion to each other ( _POI A_ is in the same area like _POI B_ but _POI C_ is in another area as _POI A_ and _POI B_ )

**Tag:** An identifier describing an object further by adding just one detail to the virtual representation in OpenStreetMap of it.

**OpenStreetMap:** "The Wikipedia of maps". The OpenStreetMap-Project aims to create an open database of spatial data released under an Open Data License allowing feeding in to geoinformation systems directly as raw.

## What kind of types of tags we can use to achieve

The idea of "Rastering regions" to offer region-based ranking service to our customers seems a great idea. But since more than just one tag can/must be utilized to get the desired data and to divide the world into small little regions that can be easily traced back and the reasoning behind the rastering can be easily understood by marketers and customers. The following list ( _OSM representation of 'regions'_ ) gives an overview of the result from my researches or researches performed by others.

### List "OSM representation of 'regions'" explained

The first column shows the representation of the information we want in OpenStreetMap. The second column says what this tag actually describes. Remarks are for annotations to this and are not mandatory.

### List "OSM representation of 'regions'"

| Tag (combination) in OSM                  | Real world representations                              | Remarks        |
| ----------------------------------------- | ------------------------------------------------------- | -------------- |
| `boundary=administrative``admin_level=10` | Subpurbs in a city                                      | only relations |
| `boundary=administrative``admin_level=8`  | A smaller commune like _Kisdorf_ in Schleswig-Holstein. | only relations |
| `boundary=postal_code`                    | area where one postal code is assigned to               | only relations |

## Conclusion

Doing some tests with Overpass Turbo searching for relations having the tags I found out that `boundary=postal_code` works best but my personal aim is to raster by communes/districts. So I need to combine two tags not clashing on each other with the objects they're being carried on:

- So I will use the query at http://overpass-turbo.eu/s/RkY (`boundary=administrative``admin_level=8` on relations ) to catch up the whole countrysite around the cities.
  
  - The query for this is as follow:
    
    ```
    /*
    This has been generated by the overpass-turbo wizard.
    The original search was:
    “boundary=administrative and admin_level=8”
    */
    [out:json][timeout:25];
    // gather results
    (
      relation["boundary"="administrative"]["admin_level"="8"]({{bbox}});
    );
    // print results
    out body;
    >;
    out skel qt;
    ```

- And then another seperate query at http://overpass-turbo.eu/s/Rl2 (`boundary=administrative``admin_level=10` on relations to catch up all regions in all cities.)
  
  - The query for this is as follow:
    
    ```
    /*
    This has been generated by the overpass-turbo wizard.
    The original search was:
    “boundary=administrative and admin_level=10”
    */
    [out:json][timeout:25];
    // gather results
    (
      relation["boundary"="administrative"]["admin_level"="10"]({{bbox}});
    );
    // print results
    out body;
    >;
    out skel qt;
    ```

- **Alternatively to the first and second bullet point** you can do that all at ones: http://overpass-turbo.eu/s/Rl3 (`boundary=administrative``admin_level=8` on relations and `boundary=administrative``admin_level=10` on relations):
  
  - The query for this is as follow (**I personally prefer this**):
    
    ```
    [out:json][timeout:25];
    // gather results
    (
      relation["boundary"="administrative"]["admin_level"="10"]({{bbox}});
      relation["boundary"="administrative"]["admin_level"="8"]({{bbox}});
    );
    // print results
    out body;
    >;
    out skel qt;
    ```

## Import procedure

1. Use one of the queries 

2. Running the query

3. Exporting result as `.osm` file

4. Feeding _osm2pgsql_ with the data in the `.osm` file.
