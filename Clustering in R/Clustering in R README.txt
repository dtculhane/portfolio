Clustering in R README
David Culhane

This project works with clustering in R given sample sets of data. The sample data files include binary classified sample data, trinary classified sample data, and data appearing to resemble Super Mario Bros. for the NES. The script in R is intended to run with these provided datasets and teach the clustering process, as well as its effects, in R.

Part 1 loads the data and creates a KNN clustering function to use on the binary and trinary datasets. Multiple clusterings are performed with various K values and these values are checked for accuracy. 

Part 2 works with the data resembling Super Mario Bros. as an unsupervised learning exercise. The kmeans function from the useful package is run for multiple K values. Mean distance from the cluster center for each point in each cluster is analyzed and plots of each clustering are made.