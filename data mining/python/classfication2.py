#%% 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold 
from sklearn.neighbors import KNeighborsClassifier 

#%%

df = pd.read_csv('../data sets/weather.nominal.csv')

# %%

X_str  = df.values[:,:-1]
y = df.values[:,-1]


#%% 
from sklearn.preprocessing import OrdinalEncoder 
enc = OrdinalEncoder()
enc.fit(X_str)
X = enc.transform(X_str)
print(X[:3])



# %%
from sklearn.naive_bayes import MultinomialNB 
clf = MultinomialNB()
cv = KFold( n_splits=10, shuffle=True , random_state=0)
cv_results = cross_val_score(clf, X, y, cv=cv )
print(cv_results.mean())
# %%

clf.fit(X,y)
test_X_str = [['sunny','hot','high',False]]

test_X = enc.transform(test_X_str)
print(clf.predict(test_X))

# %%
