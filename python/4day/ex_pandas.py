# %% 
import numpy as np 
import pandas as pd 

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
df = df [ (df['trip_duration'] > 0) &  ( df['trip_duration'] <2000)  ]

#%% 
print(df['trip_duration'].min())
print(df['trip_duration'].mean())
print(df['trip_duration'].max())


# %% 
# max day , min day 

df['week'] = df['pickup_datetime'].dt.weekday_name
print(df.groupby('week').size())

print("week count is {}".format(df['week'].value_counts()))

# lab4  tax 손님 수 
# %%
df['passenger_count'].groupby().size()


# %%
# 가장 많이 타는 시간
df["pickup_hour"]=df['pickup_datetime'].dt.strftime(%h)
print("pickup_hour count is {}".format(df['pickup_hour'].value_counts()))

# %% 
# verdor 별 fare mean 
# vendor 별 하루에 번 fare amounts


# %% 
# Taxi data와 location id

tz = pd.read_csv('taxi_zone_lookup')