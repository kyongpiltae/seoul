# %% 
import numpy as np
import matplotlib as plt
from sklearn import datasets, tree
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn import datasets, tree
from sklearn.metrics import accuracy_score,precision_score ,recall_score, f1_score
from sklearn.metrics import confusion_matrix

# %%
titanic = sns.load_dataset('titanic')

#  'pclass', 'sex’, 'age', 'sibsp', 'parch', 'fare']
print(titanic.isnull().sum())
#%% 
titanic.loc[titanic['sex']== 'female','sex'] = 1
titanic.loc[titanic['sex']== 'male','sex'] = 0
print(titanic.sex.value_counts())


# %%
dataset  = titanic[['pclass','sex','age','sibsp','parch','fare','survived']]

all = ['pclass','sex','age','sibsp','parch','fare','survived']
xvalue = ['pclass','sex','age','parch','fare','sibsp']
yvalue = ['survived']



# %%
X_test , X_train = train_test_split(dataset,test_size=0.2)
# train_test_split(arrays, test_size, train_size, random_state, shuffle, stratify)
X_test[X_test.isnull()]=0
X_train[X_train.isnull()]=0

# %%
dt = tree.DecisionTreeClassifier(max_depth=3)



dt.fit(X_train[xvalue],X_train[yvalue])


# %%

result =dt.predict(X_test[xvalue])
#%% 
accuracy_score(X_test[yvalue],result)
precision_score(X_test[yvalue],result,average='macro')
recall_score(X_test[yvalue],result,average='macro')
f1_score(X_test[yvalue],result,average='macro')

# %%
cm = confusion_matrix(X_test[yvalue],result)

# %%
