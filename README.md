# ranking-service

The service responsible for ranking the POIs

Contains everything from setting up Ranking-Database (RDB) to the rating and ranking of POI's and creating the necessary indizes. It powers the MapDiscover Ranking Service and organizes the POI's into zoom levels depending on the click count.

**rdb**: Contains the schema documentation for the table storing the POI click information depending on time as well the area data for ranking.

**ratingbyclicks**: Contains the code we need for MapDiscover Ranking Service, creation of indizes and the code for the service itself.
