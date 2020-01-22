#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency


#%% 
df = pd.read_csv('weather_nominal.csv')

# %%
df[:5]
attrs =  df.columns
print(attrs)

# %% 
contigency = pd.crosstab(df[attrs[0]],df[attrs[-1]])
print(contigency)

# %%
