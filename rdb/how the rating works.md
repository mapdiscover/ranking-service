## Definitions

**Rating:** The process of creating a ranking relative to something.

**Ranking:** Importance (weight) of the object referring to (e.g. POI). Depending on the rating process this can be relative to time, place and trigger (e.g. search)

## How we want the rating to rank POI&#39;s

The rating process depends heavily on what we really want. A rating can be relative to time, place or trigger event or even all of them. Of course, as more variables we set during ranking for time etc. as more complicated it will be. E.g. if we want the rating to consider place and time then the rating must be able to handle both cases e.g. `Hamburg, 19:00-21:00, McDonald's, Rank #1` . But if we want the rating to just consider the place then it must - of course - just be able to make the ranking relative to the place e.g. `Hamburg, McDonald's, Rank #1`.

## What do we need to count in

*   [ ] Place (Considering of place e.g. Hamburg, Schleswig-Holstein, Niedersachsen etc.
*   [ ] Time (Considering of time ranges e.g, 01:00-05:00, 05:00-08:00, 08:00-10:00, 10:00-13:00, 13:00-16:00, 16:00-19:00, 19:00-21:00, 21:00-23:00, 23:00-01:00)
*   [ ] Event (Considering of event triggers e.g. Click in search result, click on the map at the given zoom result)

### Event triggers

Event triggers are actions the user performs on MapDiscover like clicking on a POI on the map on a specified zoom, or what the user types in search and on which search result he/she clicks on. The bullet points represent just ideas:

1.  Searching for a specified POI.
2.  (Click on the POI entry in search results.)
3.  How long the user views the details view (PDV = POI details view).
4.  ~~Availability in search results.~~
5.  **Click on map (If the user clicks on a POI on the map, then that POI will receive a higher ranking)**

## Building a mockup for rating, storage of ranking result and gathering of ranking data

### Prototype version

The code of the prototype can be found [here](https://github.com/ValorNaram/ratingbyclicks). It simply reads from a file called `poiclicks.txt` which stores all click values and seperates them with a UNIX new line (`\n`). It creates a dict storing all different click values and the POI&#39;s belonging to them. Then it converts the dict into a list, loosing POI information and sorts this list by using python&#39;s `array` sort() . It gets the length of the list and divides it by DEEPLEVELS (A single value specifying in how many pieces the list should be splited: `pieces = len(list) / DEEPLEVELS`). It rounds the step to a number.

The preparation has been done: Now it literates `x` times depending on the value of DEEPLEVELS and creates the ranking. For creating the ranking it creates a dictionary once, takes the number of the current iteration, creates a dictionary item and assigns all different clicks to it that are in the given index range (at program start the start index is null and the end index equals to the value of `pieces` we calculated before).

\-- Cutting sorted list in pieces by calculating how many times the value DEEPLEVELS can be divided by. Rounding the solution and storing it to a variable `pieces`

\-- Iterating throw the range given by DEEPLEVELS ( _0_ till _DEEPLEVELS_ e.g. _0_ till _5_ )

\-- Uses the relative start index (defaults to zero on first iteration) and the relative stop index (defaults to DEEPLEVELS value on first iteration) to get the items within the index range

\-- Stores the item in the dictionary in the variable specified by the current range (e.g. from _0_ to _5_ and we are currently in iteration _2_)

SNIPPED:

```python
step = len(listSorted) / _DEEPLEVELS
pieces = round(step) -1
start = 0
stop = step
for i in range(_DEEPLEVELS): # creates an iteration (how many times a piece of items will be fetched equal to 'pieces')
	ranking[i] = listSorted[start : stop]
	start = stop
	stop += pieces
```

### Division into Modules

1.  Modul: Fetching POI&#39;s out of the database and abstraction of POI data, initiating CSV scheme, creating a working `osm_type` column by identificating Nodes, Ways and Relations. Additionally just for testing: Giving POI&#39;s random-created clicks.
2.  Modul: Creation of the POI ranking (main module).
3.  Modul: Abstraction of the ranking data to use it as a layer (Creation of ranking meta data).

#### Modul 1

In _Modul 1_ we decide which data _Modul 2_ gets to rank. In Module 1 we can decide everything about places because for every place a seperate ranking might be needed.

#### Modul 2

In _Modul 2_ we do the actual ranking. This modul does not know how to heigh because that needs to be done by the Backend module that counts the clicks.

#### Modul 3

In _Modul 3_ we do the abstraction of the ranking data. It calculates the range a specified configuration (in our case: POI&#39;s that will be shown on a specified zoom level) for using in a layer. POI-Grabber will use that data to give the Frontend just the POI&#39;s which we want to show on that zoom.
