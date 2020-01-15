path ='genesis.txt'

try:
    fh = open(path)
except:
    exit(0)


linewords = fh.readlines()

linelist = [ line.split() for line in linewords ]

worddic = dict()
for word in linelist:
    if not worddic.get(word,None):
        pass
    else:
        pass
    

worddic  ={ word k  if word in worddic k=worddic.get(word) else k=0  for word in linelist + 
print(linelist)
