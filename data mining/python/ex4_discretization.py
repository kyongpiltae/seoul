# %% 
import numpy as np
import pandas as pd 
from sklearn.utils import resample
from collections import Counter
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import KBinsDiscretizer

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import KFold,cross_val_score
import matplotlib.pyplot as plt


# %% 
df = pd.read_csv('ionosphere.csv')

#%% 
X = df.values[:,:-1]
Y = df.values[:,-1]
N= len(X)
print(Y[:2])
print(X[:2])
#%% 
discretizer = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='uniform')
discretizer.fit(X)
print(discretizer.bin_edges_)
# %%

col_i = 0 
plt.hist(X[:,col_i:col_i+1], bins=discretizer.bin_edges_[col_i],linewidth = 1.2 , edgecolor = "black")

plt.suptitle(df.columns[col_i])
plt.show()

# %%
discretizer = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='quantile')
discretizer.fit(X)
print(discretizer.bin_edges_)
col_i = 3
plt.hist(X[:,col_i:col_i+1], bins=discretizer.bin_edges_[col_i],linewidth = 1.2 , edgecolor = "black")
plt.suptitle(df.columns[col_i])
plt.show()
