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
