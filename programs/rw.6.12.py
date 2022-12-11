file = open("C:/Users/Rafist0/Documents/adventOfCode2022/programs/data/6.12.input.txt").readlines()


def strip(string):
    return string.replace('\n', '')


value = 0
marker = 14

for line in file:
    line = strip(line)
    for i, c in enumerate(line):
        if len(line[i:(i + marker)]) == len(set(line[i:(i + marker)])):
            value += (i + marker)
            break

print(value)
