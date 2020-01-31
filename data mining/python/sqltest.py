# %%
import pandas as pd 
import numpy as np 
import pymysql.cursors
#%%
IP = "localhost"
ID = 'root'
PW ='!234qwer'

# %% 
con = pymysql.connect(host = IP, user = ID, password = PW , charset='utf8mb4')

# %%
pd.read_sql("show databases",con)

# %%
with con.cursor() as cursor:
    sql = "USE classicmodels"
    cursor.execute(sql)
pd.read_sql("Show tables",con)

# %%
pd.read_sql("SELECT * From employees",con)

# %%

sql = """
select productCode , productName,textDescription
From products t1, productlines t2
WHERE t1.productline = t2.productline; """
pd.read_sql(sql,con)

# %%
sql = """
select t1.orderNumber,orderDate , SUM(priceEach)
FROM orders t1, orderdetails t2
where t1.orderNumber = t2.orderNumber
group by orderDate 
Having SUM(priceEach) > 1500; """
pd.read_sql(sql,con)


# %%
