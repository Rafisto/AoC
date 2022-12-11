file = open("C:/Users/Rafist0/Documents/adventOfCode2022/programs/data/03.12.input.txt").readlines()

value = 0
for line in file:
    line = line.replace('\n', '')
    packone = line[:(len(line) // 2)]
    packtwo = line[(len(line) // 2):]
    for c in packone:
        if c in packtwo:
            if ord(c) < 97:
                value += ord(c) - 38
            else:
                value += ord(c) - 96
            break

print(value)

value = 0

groups = []
temp = []
for i, line in enumerate(file):
    line = line.replace('\n', '')
    temp.append(line)
    if i % 3 == 2:
        groups.append(temp)
        temp = []

for group in groups:
    for c in group[0]:
        if c in group[1] and c in group[2]:
            if ord(c) < 97:
                value += ord(c) - 38
            else:
                value += ord(c) - 96
            break

print(value)
