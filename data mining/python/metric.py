#%% 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.tree import DecisionTreeClassifier

#%%

df = pd.read_csv('../data sets/glass.csv')

# %%

X  = df.values[:,:-1]
y = df.values[:,-1]
# %% 

clf = DecisionTreeClassifier(min_samples_leaf=2,random_state=0)
cv = KFold( n_splits=10, shuffle=True , random_state=0)
cv_results = cross_val_score(clf, X, y, cv=cv )
print(cv_results.mean())

# %%

metrics = ( ("acc",accuracy_score),("balanced-acc", balanced_accuracy_score)) 
for name, metric in metrics:
    print(" {} \t {}".format(name,cross_val_score(clf,X,y,scoring=make_scorer(metric)))) 
# %%
