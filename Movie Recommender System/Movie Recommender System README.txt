Movie Recommender System README
David Culhane

This project's task was to create a movie recommender system using data from MovieLens. 

The script goes along with four CSVs of data present with this file to construct a dataframe containing the movies, reviews, and tags for each movie in the dataset. This information was then grouped and aggregated ratings and number of ratings for each movie to search through.

The final product of the script accepts user-input and uses Jaccard Similarity to select a title from within the MovieLens data. Movie recommendations are then found by correlating the selected title with the data of movies and reviews described earlier. The recommendations are then printed for the user.