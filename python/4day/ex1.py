# %% 
import numpy as np 
import pandas as pd 


# %%
a = np.arange(1,11)

# b =  a.reshape(2,3)
a.sum()


# %%
pd.to_datetime('13000101', format='%Y%m%d', errors='ignore')

# %%
df=pd.read_csv("nyc.2019-01.csv")

# %%
df.describe()

# %%
df.head()

# %%
# Lab1 trip  duration 

df['dropoff_datetime']= pd.to_datetime(df['tpep_dropoff_datetime'])
df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])

# %% 
df['trip_duration'] = (df['dropoff_datetime'] - df['pickup_datetime'])
df['trip_duration'] = df['trip_duration'].dt.total_seconds()/60
df.head()
# %% 
# lab2 ave min max 
df['trip_duration'].min()
df['trip_duration'].mean()
df['trip_duration'].max()
#%% 
# pick up by day 
df1 = df [ (df['trip_duration'] > 0) &  ( df['trip_duration'] <2000)  ]

#%% 
print(df1['trip_duration'].min())
print(df1['trip_duration'].mean())
print(df1['trip_duration'].max())


# %% 
# max day , min day 
df1['week'] = df1['pickup_datetime'].dt.weekday_name
print(df1.groupby('week').size())


# lab4  tax 손님 수 


# %%
