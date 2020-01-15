import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
x = [[ i ] for i in range(10) ]
y = [[ np.random.random()*10 ] for _ in range(10) ]
regr = linear_model.LinearRegression()
regr.fit(x, y)