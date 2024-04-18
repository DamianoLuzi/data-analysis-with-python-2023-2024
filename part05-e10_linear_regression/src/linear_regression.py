#!C:\Python311\python.exe

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    x = x[:,np.newaxis] #making x into a matrix
    model = LinearRegression(fit_intercept = True)
    model.fit(x,y)
    xfit=np.linspace(0,10,50)[:,np.newaxis]
    yfit = model.predict(xfit)
    return model.coef_[0],model.intercept_
    
def main():
    n = 50
    x = np.linspace(0,10,n) # start - stop - # of samples
    y = 4*x**2-8*x+2*np.random.randn(n)
    coefficients, intercept = fit_line(x,y)
    print(f"Slope: {coefficients}")
    print(f"Intercept: {intercept}")

    yfit = coefficients*x + intercept
    plt.plot(x, y, 'o')
    plt.plot(x, yfit)
    plt.show()
    
if __name__ == "__main__":
    main()
