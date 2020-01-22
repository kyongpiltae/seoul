# %%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


# %% 
age = np.array([20,25,27,32,45,49,52,57,60,62])
fat = np.array([7 ,8 ,11,20,15,35,40,28,31,19])

# %%
print("mean : {} , std: {} , ".format(age.mean(),age.std()))

# %%
print("mean : {} , std: {} , ".format(fat.mean(),fat.std()))

# %%

print("mean : {} , std: {} , ".format(age.mean(),age.std(ddof=1)))


# %%
print("mean : {} , std: {} , ".format(fat.mean(),fat.std(ddof=1)))


# %%

a = np.array([[22,1,42,10],[20,0,36,8]])
L1_norm = np.linalg.norm(a, axis=1, ord=1)
print(L1_norm)
# %% 
a = np.array([[22,1,42,10],[20,0,36,8]])
L2_norm = np.linalg.norm(a, axis=1, ord=2)
print(L2_norm)
print(L2_norm.shape)



# %%
from scipy.spatial import distance
m3 = distance.minkowski([22,1,42,10],[20,0,36,8], 3)
print(m3)

# %%
