# %% 
import numpy as np
import pandas as pd 
from sklearn.utils import resample
from collections import Counter



# %%
X_toy = [1,2,3,4,5]
Y_toy = [6,7,8,9,10]


X_s , y_s = resample(X_toy,Y_toy, replace = True, n_samples =7 , random_state =0)

print(X_s)
print(y_s)

# %%
X_s , y_s = resample(X_toy,Y_toy, replace = False, n_samples =5 , random_state =0)

print(X_s)
print(y_s)

# %%


df = pd.read_csv('glass.csv')

#%% 
X = df.values[:,:-1]
Y = df.values[:,-1]
N= len(X)
X_s , y_s = resample(X,Y, replace = False, n_samples =int(N*0.2) , random_state =0)

print(X_s)
print(y_s)

# %%
c = Counter(y_s)
print(c)

# %%

for i in range(5):
    X_s , y_s = resample(X,Y, replace = False, n_samples =int(N*0.2) , random_state =i)
    c = Counter(y_s)
    print(c)

# %%
X_s , y_s = resample(X,Y, replace = False, n_samples =int(N*0.2) , random_state =0,stratify =Y )
c = Counter(y_s)
print(c)

# %%
for i in range(5):
    X_s , y_s = resample(X,Y, replace = False, n_samples =int(N*0.2) , random_state =i,stratify =Y)
    c = Counter(y_s)
    print(c)
