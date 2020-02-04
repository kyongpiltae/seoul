# %% 
import numpy as np
import pandas as pd 
from sklearn.utils import resample
from collections import Counter
from sklearn.preprocessing import MinMaxScaler


# %% 
df = pd.read_csv('glass.csv')

#%% 
X = df.values[:,:-1]
Y = df.values[:,-1]
N= len(X)
#%% 
normalizer = MinMaxScaler(X)
X_norm = normalizer.fit_transform(X)

# %%
print(X_norm)
print(nomalizer.scale)
# %%
