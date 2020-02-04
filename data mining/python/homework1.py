
#%% 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
# %%

data =  [[2,4],[6,1],[1,8],[6,3],[3,6],[7,5],[6,6],[7,9],[8,9]]
X = np.array(data)

#%%
from sklearn.cluster import AgglomerativeClustering

for i, linkage in enumerate(('single','complete')):
    clustering = AgglomerativeClustering(linkage = linkage, n_clusters=4)

    y_pred = clustering.fit_predict(X)
    plt.figure(i+1,figsize=(5,5))
    plt.title(linkage + " cluster : 4")
    plt.scatter(X[:,0],X[:,1],s=30,c=y_pred,cmap='tab20')
plt.show()

# %%
#for i, linkage in enumerate(('single','complete','average','ward')):
for i, linkage in enumerate(('single','complete')):

    for j in range(2,5):
        clustering = AgglomerativeClustering(linkage = linkage, n_clusters=j)

        y_pred = clustering.fit_predict(X)
        plt.figure(i*3+(j-1),figsize=(5,5))
        plt.title(linkage + "distance  cluster number: " + str(j))
        plt.scatter(X[:,0],X[:,1],s=30,c=y_pred,cmap='tab20')
plt.show()


# %%
