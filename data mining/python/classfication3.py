#%% 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold 
from sklearn.neighbors import KNeighborsClassifier 


from sklearn.ensemble import RandomForestClassifier 



# %% 
df = pd.read_csv('../data sets/glass.csv')
X = df.values[:,:-1]
y = df.values[:,-1]

cv = KFold( n_splits=10, shuffle=True , random_state=0)
# %% 

random = RandomForestClassifier(criterion="entropy", min_samples_leaf=2, n_estimators=200, random_state=0)
print(cross_val_score(random,X,y, cv = cv ).mean())

# %%
from sklearn.tree import DecisionTreeClassifier 

tree = DecisionTreeClassifier(criterion="entropy", min_samples_leaf=2, random_state=0)
print(cross_val_score(tree,X,y, cv = cv ).mean())

# %%
from sklearn.ensemble import BaggingClassifier
bag = BaggingClassifier( n_estimators=200, random_state=0)
print(cross_val_score(bag,X,y, cv = cv ).mean())

# %% 
from sklearn.ensemble import AdaBoostClassifier 
ada = AdaBoostClassifier( n_estimators=200, random_state=0)
print(cross_val_score(ada,X,y, cv = cv ).mean())
# %%
