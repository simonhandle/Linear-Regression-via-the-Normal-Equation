import math
import numpy as np
import pandas as pd

class LinearRegression:
    def fit(self, X, y):
        y = np.array(y)

        X = np.array(X)
        X = np.insert(X,0,1,axis=1)

        X_T = X.T
        X_T_y = X_T @ y
        X_T_X = X_T @ X
        X_T_X_inv = np.linalg.inv(X_T_X)

        self.a = X_T_X_inv @ X_T_y

    def predict(self,X):
        X = np.array(X)
        X = np.insert(X,0,1,axis=1)
        y_pred = X @ self.a
        return np.array(y_pred)
    
    def mse(self,y_true,y_pred):
        dev = (y_pred - y_true)**2
        mse = sum(dev)/len(dev)
        return mse
    
    def mae(self,y_true,y_pred):
        dev = abs(y_pred - y_true)
        mae = sum(dev)/len(dev)
        return mae