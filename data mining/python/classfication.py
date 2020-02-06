#%% 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold 
from sklearn.neighbors import KNeighborsClassifier 

#%%

df = pd.read_csv('../data sets/glass.csv')

# %%

X = df.values[:,:-1]
y = df.values[:,-1]

# %%

clf = KNeighborsClassifier(n_neighbors=10,weights='uniform',metric='euclidean')
cv = KFold(n_splits=10,shuffle=True,random_state=0)

cv_results = cross_val_score(clf,X,y,cv=cv)
print(cv_results.mean())

# %%

for i, val in enumerate([20,5,1]):
    clf = KNeighborsClassifier(n_neighbors=val,weights='uniform',metric='euclidean')
    cv = KFold(n_splits=10,shuffle=True,random_state=0)
    cv_results = cross_val_score(clf,X,y,cv=cv)
    print( "{} neighbors's result is {}".format(val,cv_results.mean()))

# %%

from sklearn import tree 
import graphviz 
from sklearn.preprocessing import OneHotEncoder 
import numpy as np 
import pandas as pd 

df = pd.read_csv('../data sets/weather.nominal.csv')
X = df.values[:,:-1]
y = df.values[:,-1]
# %% 
enc = OneHotEncoder(handle_unknown="ignore")
enc.fit(X)
# %% 
en_X = enc.transform(X).toarray()
en_X 

# %% 

categories = []
for x in enc.categories_:
    categories += list(x)
print(categories)

# %%

clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(en_X,y)

print(clf.classes_)

# %% 
test = [['overcast','mild','high',True]]
en_test = enc.transform(test).toarray()

print(en_test)

pred_y = clf.predict(en_test)
print(pred_y)
pred_prob = clf.predict_log_proba(en_test)
print(pred_prob)


# %% 
cv = KFold( n_splits=10, shuffle=True , random_state=0)
cv_results = cross_val_score(clf, en_X, y, cv=cv )

print(cv_results.mean())
# %%
dot_data = tree.export_graphviz(clf, out_file=None, feature_names=categories, class_names=clf.classes_, filled=True, special_characters=True)
graph = graphviz.Graph(dot_data)
graph

# %%


clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3, min_samples_split=3 , min_samples_leaf=2)



# %% 
def zeroR(y,test):
    output_values = [label for label in y]
    prediction = max(set(output_values),key=output_values.count)
    predicted = [ prediction for i in range(len(test))]
    return predicted 

r= zeroR(y,[['overcast','cool','high',True]])
print (r)

# %%
from sklearn.model_selection import train_test_split 

df = pd.read_csv('../data sets/diabetes.csv')
X = df.values[:,:-1]
y = df.values[:,-1]
enc = OneHotEncoder(handle_unknown="ignore")
enc.fit(X)
en_X = enc.transform(X).toarray()
en_X 

# %%

X_train , X_test ,y_train, y_test =train_test_split(X,y,test_size=0.1)
hit = 0 
for i in range(len(y_test)):
    predicted = ZeroR(y_train, X_test[i:i+1])
    if(predected == y_test[i:i+1]):
        hit += 1

print(hit/len(y_test))




# %% 

clf = tree.DecisionTreeClassifier(criterion="entropy")
cv = KFold( n_splits=10, shuffle=True , random_state=0)
cv_results = cross_val_score(clf, en_X, y, cv=cv )
print(cv_results.mean())


clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3, min_samples_split=3 , min_samples_leaf=2)
cv = KFold( n_splits=10, shuffle=True , random_state=0)
cv_results = cross_val_score(clf, en_X, y, cv=cv )
print(cv_results.mean())


# %% 
from scipy.io import arff

data, meta = arff.loadarff('../data sets/breast-cancer.arff')
df = pd.DataFrame(data)
df.head()
# %% data
#df = pd.read_csv('../data sets/breast-cancer.csv')
X = df.values[:,:-1]
y = df.values[:,-1]

#%% 
enc = OneHotEncoder(handle_unknown="ignore")
enc.fit(X)
en_X = enc.transform(X).toarray()
en_X 
categories = []
for x in enc.categories_:
    categories += list(x)
print(categories)

# %% 
clf = tree.DecisionTreeClassifier(criterion="entropy")
cv = KFold( n_splits=10, shuffle=True , random_state=0)
cv_results = cross_val_score(clf, en_X, y, cv=cv )
print(cv_results.mean())

# %% 

clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3, min_samples_split=3 , min_samples_leaf=2)
cv = KFold( n_splits=10, shuffle=True , random_state=0)
cv_results = cross_val_score(clf, en_X, y, cv=cv )
print(cv_results.mean())



# %%
