# kombinieren

data = open("C:/Users/Rafist0/Documents/adventOfCode2022/programs/data/7.12.input.txt").read().split('\n')

directories = {}
dirlist = []
cd = ''
for line in data:
    if '$ cd' in line and '..' not in line:
        dir = line.replace('$ cd ', '')
        cd += dir
        if cd not in directories:
            directories[cd] = []
        dirlist.append(dir)

    elif '$ cd' in line and '..' in line:
        cd = cd.removesuffix(dirlist[len(dirlist) - 1])
        dirlist.pop(len(dirlist) - 1)

    elif '$ cd' not in line and '$ ls' not in line:
        if 'dir' in line:
            dir = line.replace('dir ', '')
            directories[cd + dir] = []
        else:
            size, name = line.split()
            directories[cd].append((int(size), name))

total_size = {directory: 0 for directory in directories}

for directory in directories:
    for item in directories[directory]:
        if type(item) == tuple:
            total_size[directory] += item[0]

for key in total_size:
    for directory in directories:
        if key in directory and key != directory:
            total_size[key] += total_size[directory]

total = 0

empty_space = 70000000 - max(total_size.values())
space_needed = 30000000 - empty_space
temp = []

for directory in total_size:
    if total_size[directory] <= 100000:
        total += total_size[directory]
    if total_size[directory] >= space_needed:
        temp.append(total_size[directory])

print(total)
print(min(temp))
