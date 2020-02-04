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
from sklearn.cluster import DBSCAN 
dbscan = DBSCAN(eps=0.05 , min_samples=20)

y_pred = dbscan.fit_predict(X)
print(y_pred[:10])

# %%
for i, (eps , min_samples) in enumerate(((0.05,20),(0.06,20),(0.06,15),(0.06,6))):
    dbscan = DBSCAN(eps=eps , min_samples=min_samples)
    y_pred = dbscan.fit_predict(X)
    plt.figure(i+1,figsize=(5,5))
    plt.scatter(X[:,0],X[:,1],s=4,c=y_pred,cmap='tab20')
    plt.title("eps: {} min_samples: {}".format(eps,min_samples))
plt.show()



# %%
from sklearn.cluster import OPTICS, cluster_optics_dbscan 
optics = OPTICS(min_samples=5, xi=0.1,metric='euclidean')

cluster = optics.fit(X)
y_pred = cluster_optics_dbscan(reachability = cluster.reachability_, core_distances = cluster.core_distances_, ordering = cluster.ordering_, eps=0.1)
plt.title("Optics with dbscan")
plt.scatter(X[:,0],X[:,1],s=4,c=y_pred,cmap='tab20')
plt.show()

#%% 
from sklearn.cluster import OPTICS, cluster_optics_dbscan 
optics = OPTICS(min_samples=5, xi=0.1,metric='euclidean')
y_pred = optics.fit_predict(X)
plt.scatter(X[:,0],X[:,1],s=4,c=y_pred,cmap='tab20')
plt.title("Optics without dbscan")
plt.show()
# %%
for i, xi in enumerate((0.1,0.3,0.5,0.7,0.9)):
    optics = OPTICS(min_samples=5, xi=xi,metric='euclidean')
    cluster = optics.fit(X)
    y_pred = cluster_optics_dbscan(reachability = cluster.reachability_, core_distances = cluster.core_distances_, ordering = cluster.ordering_, eps=0.1)
    plt.figure(i+1,figsize=(5,5))
    plt.scatter(X[:,0],X[:,1],s=4,c=y_pred,cmap='tab20')
    plt.title("xi : {} ".format(xi))
plt.show()


# %%
from sklearn.mixture import GaussianMixture 
em =  GaussianMixture(n_components=4,max_iter=20,random_state=0)
y_pred = em.fit_predict(X)
print(em.warm_start,'\n' , em.means_,"\n", em.covariances_)
plt.scatter(X[:,0],X[:,1],s=4,c=y_pred,cmap='tab20')
plt.show()

# %%
