#%% 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
#%% 


df = pd.read_csv('../data sets/cluster2.csv')

# %%
# %matplotlib inline

print("Dimesions of the data = {}".format(df.shape))

# %%
X= df.values
print(X[:5])
# %% 
plt.figure(figsize=(5,5))
plt.scatter(X[:,0],X[:,1],s=4)

plt.show()

# %%
camp="tab10"
from sklearn.cluster import KMeans 
k_means = KMeans(n_clusters=4 , random_state=0  )


# %%
y_pred = k_means.fit_predict(X)
print(y_pred[:10])

# %%
print(k_means.cluster_centers_)

# %%
plt.figure(figsize=(5,5))
plt.scatter(X[:,0],X[:,1],s=4,c=y_pred,cmap='tab10')

plt.show()

# %%

for i, x in enumerate(("A","B","C")):
    print (i,x)

# %%
from sklearn.cluster import AgglomerativeClustering

for i, linkage in enumerate(('single','complete')):
    clustering = AgglomerativeClustering(linkage = linkage, n_clusters=4)

    y_pred = clustering.fit_predict(X)
    plt.figure(i+1,figsize=(5,5))
    plt.scatter(X[:,0],X[:,1],s=4,c=y_pred,cmap='tab10')
plt.show()

# %%
for i, linkage in enumerate(('single','complete','average','ward')):

    for j in range(2,5):
        clustering = AgglomerativeClustering(linkage = linkage, n_clusters=j)

        y_pred = clustering.fit_predict(X)
        plt.title(linkage + " cluster " + str(j))
        plt.figure(i*3+(j-1),figsize=(5,5))
        plt.scatter(X[:,0],X[:,1],s=4,c=y_pred,cmap='tab10')
plt.show()

# %%
from sklearn.cluster import Birch
brc = Birch(threshold=0.5, n_clusters=None , branching_factor=50)
y_pred = brc.fit_predict(X)
plt.figure(figsize=(5,5))
plt.title("birch 0.5 ")
plt.scatter(X[:,0],X[:,1],s=4,c=y_pred,cmap='tab10')
plt.show()


# %%
brc = Birch(threshold=0.1, n_clusters=None , branching_factor=50)
y_pred = brc.fit_predict(X)
plt.figure(figsize=(5,5))
plt.title("birch 0.1 ")
plt.scatter(X[:,0],X[:,1],s=4,c=y_pred,cmap='tab20')
plt.show()
# %%
brc = Birch(threshold=0.5, n_clusters=4 , branching_factor=50)
y_pred = brc.fit_predict(X)
plt.figure(figsize=(5,5))
plt.title("birch 0.4  n_cluster = 4 ")
plt.scatter(X[:,0],X[:,1],s=4,c=y_pred,cmap='tab20')
plt.show()

# %%
brc = Birch(threshold=0.1, n_clusters=4 , branching_factor=50)
y_pred = brc.fit_predict(X)
plt.figure(figsize=(5,5))
plt.title("birch 0.1  n_cluster = 4 ")
plt.scatter(X[:,0],X[:,1],s=4,c=y_pred,cmap='tab20')
plt.show()

# %%

for i ,v in enumerate((0.5, 0.1,0.05,0.01)):
    print(i,v)
    brc = Birch(threshold=v, n_clusters=None , branching_factor=50)
    y_pred = brc.fit_predict(X)
    plt.figure(i+1,figsize=(5,5))
    plt.title("birch  threshold = " + str(v))
    plt.scatter(X[:,0],X[:,1],s=4,c=y_pred,cmap='tab20')
plt.show()

# %%
for i ,v in enumerate((0.5, 0.1,0.05,0.01)):
    print(i,v)
    brc = Birch(threshold=v, n_clusters=4 , branching_factor=50)
    y_pred = brc.fit_predict(X)
    plt.figure(i+1,figsize=(5,5))
    plt.title("birch n_cluster=4  threshold = " + str(v))
    plt.scatter(X[:,0],X[:,1],s=4,c=y_pred,cmap='tab20')
plt.show()

# %%
