from numpy import isnan
from pandas import read_csv, DataFrame
from sklearn.impute import SimpleImputer

# Load the data
df = read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/horse-colic.csv',
              header=None,
              na_values='?',)

# Show the first 5 rows of the data
df.head()

# Define X (Predictor variables) and y (Target variable)
dt = df.values
ix = [i for i in range(dt.shape[1]) if i != 27]
X, y = dt[:, ix], dt[:, 27]

# Show count of missing values of X (before imputation)
sum(isnan(X).flatten())

# Define imputer
imp = SimpleImputer(strategy='median')

# Fit and transform imputer on the dataset
Xtrans = imp.fit_transform(X)

# Show count of missing values of Xtrans (after imputation)
sum(isnan(Xtrans).flatten())

# Convert NumPy array to Pandas DataFrame
Xtrans = DataFrame(data=Xtrans)

# Show the first 5 rows of the data with imputed values
Xtrans.head()
