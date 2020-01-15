# %%

s = 'hi hello world'
print(s.split())
# %%
l = ['aaa','bbb','ccc']

''.join(l)
'*'.join("abcd")

# %%
#list comprehention

a = [1,2,4,5,6,7,8]
b = [10,11,12,13,14]

n = [ [(i , j) for i in a] for j in b ]

print(n)


# %%
