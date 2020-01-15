# http://csl.snu.ac.kr/sleds/
'''

'''
#%%
a = 1

type(a)

id(a)

# %%
a = 1
b = 1

id(a)
id(b)
print(id(a) == id(b))
# %%
a = 5000
b = 5000
id(a)
id(b)
print(id(a) == id(b))
print(a == b )
print(a is b ) # comparing id

if ( a is None):
    print("is operator is recommneded cause speed and reference  ")


# %%
d = 0.1
d+d+d+d+d+d+d+d+d+d

# %%
pi = 3.14159
VeryLarge = 1e20
x = (pi + VeryLarge)- VeryLarge
y = pi + (VeryLarge- VeryLarge)
# %%
pi = 3.14159
VeryLarge = 1e20
x = (pi + VeryLarge)- VeryLarge
y = pi + (VeryLarge- VeryLarge)

import math
math.isclose(x,y)

#%%

a = [ 4,1,9,0]
c = a.copy()
b = a
a[2] =7

print(a)
print(b)

c = a.copy()
print(c)


print(a.sort())
print(sorted(a))

# %%
