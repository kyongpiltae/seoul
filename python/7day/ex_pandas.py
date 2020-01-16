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
from sklearn import preprocessing
import pandas as pd
from sklearn import linear_model

# %%
df = pd.read_csv("BostonHousing.csv")


#%% 

df.head(5)
# %%
dataset  = df

all = ['pclass','sex','age','sibsp','parch','fare','survived']
xvalue = ['LSTAT']
yvalue = ['MEDV']




# %%
X_test , X_train = train_test_split(dataset,test_size=0.2)
# train_test_split(arrays, test_size, train_size, random_state, shuffle, stratify)
X_test[X_test.isnull()]=0
X_train[X_train.isnull()]=0

# %%
dt =linear_model.LinearRegression()
#dt = tree.DecisionTreeClassifier(max_depth=3)



dt.fit(X_train[xvalue],X_train[yvalue])


# %%

result =dt.predict(X_test[xvalue])
#%% 
import matplotlib.pyplot as plt
plt.scatter(X_test[yvalue], result)
plt.xlabel("real")
plt.ylabel("predict")
plt.title(" real and predict")
plt.show()

# %% 

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(X_test[yvalue], result)
print(mse )
# %%
