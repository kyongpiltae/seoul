# %% 
import pandas as pd 
import numpy as np 
import pyfpgrowth

# %% 
df = pd.read_csv('../data sets/supermarket.csv')

# %%



transaction = []
for row in df.values:
    
    tmp=[]
    for i in range(len(row)-1):
        if row[i] == 't':
            tmp.append(i)
    
    #tmp= row[:-1].nonzero()[0].tolist()
    print(row[:-1].nonzero()[0])
    transaction.append(tmp)

print(len(transaction))

# %%
min_sup = 0.3
confidence = 0.75
patterns = pyfpgrowth.find_frequent_patterns(transaction,int(min_sup*len(transaction)))

# %%


print(patterns)

# %%
rules = pyfpgrowth.generate_association_rules(patterns,confidence)
print(rules)

# %%

sorted_rules = sorted(rules.items(), key=lambda t: t[1][1])

print(sorted_rules)

# %%
k = 10
topk_rules = [(rule[0],rule[1][0],rule[1][1]) for rule in sorted_rules[:k]]

print(topk_rules)

# %%
