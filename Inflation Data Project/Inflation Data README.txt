Inflation Datapreparation README
David Culhane

This project intended to combine data from various sources (a flat file, data scraped from a website, and data from a called API) into a single dataset. The central theme for the data was data regarding inflation around the globe. The flat data came in the form of a CSV from the World Bank, the scraped web data came from Wikipedia (stored in the file to future-proof the code from future edits of the site) and used UN inflation data, and the API data came from NewsAPI.

The idea was to bring all of the data together into a single dataframe where each row was a single country with periodic data from the World Bank and UN as well as a cell containing a list of news aritcles selected from a NewsAPI call. Information about inflation can be gleaned from the data provided by the World Bank and UN while the list of text articles for each country could be analyzed for additional contextual information.

Each script for the project addressed a different aspect: working with the flat file, scraping and working with the web data, calling the NewsAPI and working with that data, and merging all three indivdual datasets together.

The project itself hit a snag towards the end due to the limited scope of free access to NewsAPI. Only 50 calls could be made in a 12 hour period with a limit of 100 calls in a day within the free tier of use. This limited the dataset to only 50 countries since the script was intended to be run once due to the original project being academic in nature. However, the premise of the API call outside of an educational setting could end up being adapted. An adaptation of this portion of the script could work with subsetting the various countries and calling a user's input to specify which subset of up to 50 countries should be called for with the NewsAPI function. This data could then be stored and merged with previously called data until a complete dataset is assembled.

After the data is assembled, it is stored in a database using SQLite3. This database is then queried for a few countries and visualizations of thier data.