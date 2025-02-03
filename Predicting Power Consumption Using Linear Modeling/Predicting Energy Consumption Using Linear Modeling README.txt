Predicting Power Consumption Data Using Linear Modeling README
David Culhane

This project uses data acquired on Kaggle to model power consumption for buildings based on a number of features. Lasso and Ridge models were created with a search space of values for the alpha hyperparameter to evaluate which model would be best.

Helper functions were created to create models, store their predictions, and store metric data for evaluating the model across the alpha search space. Residual values were computed and stored for each model as well for model evaluation.

Scikit-Learn is heavily featured in the script and is used for data standardization and model creation. Matplotlib and Seaborn are used for graph creation within the script, though the processed data is exported to Excel to allow for the creation of higher quality visualizations in Power BI.

The Ridge models provided sweet-spots (dips in error metrics) for the alpha hyperparameters while the lasso models decayed quickly as the value of alpha increased. This decay in quality by the Lasso models led to the addition of basic linear regression models to the project. The basic linear regression models also showed promise but their model metrics were only slightly worse than those of the Ridge models using a sweet-spot alpha value. Residual values for the Ridge and basic linear regression models stayed within 1 kWh of actual values. Both models would have promise in a real-world situation, assuming an energy producer had access to the fields of data listed in the training and testing datasets.