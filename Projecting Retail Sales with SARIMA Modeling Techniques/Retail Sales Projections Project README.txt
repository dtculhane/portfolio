Retail Sales Projections Project README
David Culhane

This project intends to use a large retail sales dataset to project retail sales in Python. The end product used SARIMA models from statsmodels and pmdarima to make the projections and were compared to each other.

The data used was sourced from Kaggle and came in three flat sources describing weekly sales at numerous stores, across numerous departments in each store, and information regarding economic metrics in each store's area. 

Data preparation involved merging the data to make sure each row represented a single store and department with contextual economic information. Data unhelpful for modeling was removed. This included information about gas prices, which were the same for every store and department every week (likely a national instead of regional average) and five "MarkDown" fields which were each more than 60% empty (replacing these values would have done more harm than good to the data). 

Modeling was done with SARIMA models from the statsmodels and pmdarima libraries. Both were done in order to compare their projections and metrics to see which would be better. The models performed similarly and both suffered somewhat from less data than originally intended. Due to the nature of SARIMA modeling, only sequential data fom one store/department combination could be fed into a single model. The large size of the dataset was due to the large number of departments across the dataset. This would work well if the intention was to create a model for every department but that would've been a herculean task. It was decided to make two models each for three departments, each one coming from a different store type in the dataset, for a total of six models. Each model made decent and understandable predictions given that the modeling data for a given department spanned 2.75 years. Having more data by spanning a larger amount of time would have benefitted the models greatly.
