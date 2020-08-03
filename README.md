# Data Imputation Techniques
Data imputation refers to the technique of filling up missing values in the dataset. Missing values are quite common in real-world datasets. Training your model with missing values results in inaccurate predictions. This is why data imputation techniques are a must-know for anyone in the field of ML, DL, or Data Science. 

In this repository, three (03) such techniques known to me so far have been applied, namely Simple Imputation, KNN (k-Nearest Neighbor) Imputation, and Iterative Imputation. All of these techniques have been applied through the popular Scikit-Learn machine learning library.

# SimpleImputer
As the name implies, it is one of the simplest imputation techniques. SimpleImputer works for both numeric and string data. Although, there are further 4 techniques in SimpleImputer to impute data, statistical techniques, like filling the missing values with the mean and median of the non-missing data are among the most common. However, they both are limited to numeric data. I can call SimpleImputer a fixed imputation technique since it will return the same values for the same data. For further info, refer to the respective API reference guide page here: https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html

# KNNImputer
As opposed to SimpleImputer, KNNImputer is not a fixed imputation technique. Rather, the resulting data depends on the number of neighbors you specify. Here, the term 'neighbors' refers to the non-missing values near the missing data. For instance, if I specify 2 neighbors, I shouldn't expect to get the same results when I specify the number of neighbors to be 5. For further info, refer to the respective API reference guide page here: https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html

# IterativeImputer
This technique is experimental so you can expect to be getting different set of values. The API Reference Guide page suggests that IterativeImputer imputes the data in a 'round-robin' fashion. The API Reference Guide Page can be found here: https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html

# Missing Values Representation in the Dataset

The dataset used in the code contains missing or null values marked with a question mark '?'.
