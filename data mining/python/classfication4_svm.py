# %% 
from sklearn import tree ,svm
from sklearn.preprocessing import OneHotEncoder 
from sklearn.model_selection import cross_val_score

import numpy as np 
import pandas as pd 


df = pd.read_csv('../data sets/vote.csv')
X = df.values[:,:-1]
y = df.values[:,-1]
# %% 
enc = OneHotEncoder(handle_unknown="ignore")
enc.fit(X)
# %% 
en_X = enc.transform(X).toarray()
en_X 
cv = KFold( n_splits=10, shuffle=True , random_state=0)

# %%
clf = svm.SVC(kernel='linear',gamma='auto')
scores = cross_val_score(clf,en_X,y,cv=10)
print(scores)
# %%
