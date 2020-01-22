
# %%

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
# %% 
datafolder = "..\\daata sets\\"

# %%
df = pd.read_csv('glass_missing.csv')
print(df[:5])
# %%
X = df.values[:,:-1]
Y = df.values[:,-1]

# %%
imp = SimpleImputer(missing_values=np.nan,strategy='mean')
X_new = imp.fit_transform(X)
print(X_new[:5])
#%% 
method = ['mean','median','most_frequent','constant']

for i in range(len(method)):
    imp = SimpleImputer(missing_values=np.nan,strategy=method[i],fill_value=10)
    X_new = imp.fit_transform(X)
    print(method[i])
    print(X_new[:5])


# %%
# categorical 
df = pd.read_csv('weather.nominal_missing.csv')

#%%
print(df[:5])
df.get("temperature").value_counts()
# %%


X = df.values[:,:-1]
Y = df.values[:,-1]

# %%
imp = SimpleImputer(missing_values=np.nan,strategy='most_frequent')
X_new = imp.fit_transform(X)
print(X_new[:5])

# %%
# categorical 

# %%
imp = SimpleImputer(missing_values=np.nan,strategy='constant')
X_new = imp.fit_transform(X)
print(imp.statistics_)



# %%
