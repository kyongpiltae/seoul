name = 'genesis.txt'
fh = open(name)
contents = fh.read()

print(len(contents))

fh = open(name)

for line in fh:
    if line.startswith('1:'):
        line = line.rstrip()
        print(line)
fh = open(name)
for line in fh:
    if not line[0].isdigit():
        continue
        line = line.rstrip()
        print(line)
fh = open(name)
for line in fh:
    if 'hevean' in line:
        line = line.rstrip()
        print(line)