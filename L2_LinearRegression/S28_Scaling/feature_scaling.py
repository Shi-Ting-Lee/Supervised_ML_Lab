import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler

# Assign the data to predictor and outcome variables
# TODO: Load the data
data = pd.read_csv('data.csv', header = None)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# TODO: Create the standardization scaling object.
scaler = StandardScaler() 

# TODO: Fit the standardization parameters and scale the data.
X_scaled = scaler.fit_transform(X)

# TODO: Create the linear regression model with lasso regularization.
# fit model
lasso_reg = Lasso()
lasso_reg.fit(X_scaled, y)

# TODO: Retrieve and print out the coefficients from the regression model.
reg_coef = lasso_reg.coef_
print(reg_coef)

