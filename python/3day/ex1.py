#%%
import numpy as np 
import matplotlib.pyplot as plt
# %%  
x = np.array([[1,2,3],[4,5,6,]],int)

print(x)

print(type(x))

print(x.shape)
print(x.dtype)


test =np.array(["abcdef","abcdef"])

# %%

f = np.full(5,2)

f1 = np.full((2,3),-1,float)
f2 = np.full_like(f1,2)
f3 = np.empty((1,5))
f4 = np.empty_like(f2)

# %%
f5 = np.zeros((3,5))
f6 = np.zeros_like(f1)
f7 = np.identity(4)

# %%

n1 = np.arange(10,30,5)
n2 = np.arange(0,2,0.3)
n3 = np.arange(8.0,8.4,0.05)

l1 = np.linspace(0,100,5) # linear 
l2 = np.logspace(0,1,11)  # log space
l3 = np.geomspace(1,1000,4)




# %%
import numpy as np
import matplotlib.pyplot as plt
pts = np.arange(-5, 5, 0.01)
x, y = np.meshgrid(pts, pts)
z = np.sqrt(x**2 + y**2)
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.show()

# %%
a= np.arange(6)
print(a.shape)

a.reshape(2,3)

print(a.shape)

a.resize(2,3)
print(a.shape)
a.flatten()
print(a.shape)
a.reshape(1,-1)
print(a.shape)
# %%
a = np.arange(6)
a.transpose()
b = a.reshape(3,2)
#%% 
y = np.arange(35).reshape(5,7)
print(y)

# %%


alph ="abcdefghijklmnopqrstu"

def encode(data):
    encoded = np.array(list( np.eye(1,27, alph.index(c))[0] for c in data ))
    return encoded


print(encode("abc"))

# %%
