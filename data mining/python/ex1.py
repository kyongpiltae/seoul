# %% 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# %% 
df = pd.read_csv('iris.csv')

# %%
# df.values  -> np.array 속성.
X = df.values[:,:-1].astype(np.float32)
y = df.values[:,-1]

# %%

X.max(axis=0) # columns
X.min(axis=0) # axis =0 , 0번축을 고정하라 
np.percentile(X,70,axis=0)
np.percentile(X,50,axis=0) # 50th percentile
np.percentile(X,100,axis=0)
np.percentile(X,0,axis=0)

# %%
X.mean(axis=0)
X.std(axis=0)
X.var(axis=0)

# %%
plt.figure(figsize=(5,10))
plt.boxplot(X)
plt.show()

# %%
plt.figure(figsize=(5,10))
plt.boxplot(X[:,1])
plt.show()

# %%
columns = df.columns[:-1]
plt.figure(figsize=(7,7))
plt.xlabel(columns[0])
plt.ylabel(columns[1])
plt.scatter(X[:,0],X[:,1])
plt.show()

# %%

fig ,axs = plt.subplots(4,4,figsize=(20,20)) # 20 inch

for i in range(4):
    for j in range(4):
        axs[i,j].set(xlabel = columns[i],ylabel=columns[j])
        axs[i,j].scatter(X[:,i],X[:,j])

plt.show()

# %%
