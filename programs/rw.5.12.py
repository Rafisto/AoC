file = open('C:/Users/Rafist0/Documents/adventOfCode2022/programs/data/03.12.input.txt').readlines()

stacks = [
    'PGRN',
    'CDGFLBTJ',
    'VSM',
    'PZCRSL',
    'QDWCVLSP',
    'SMDWNTC',
    'PWGDH',
    'VMCSHPLZ',
    'ZGWLFPR'
]

# stacks = [
#     'NZ',
#     'DCM',
#     'P'
# ]

file = file[10:]

for line in file:
    line = line.replace('\n', '')
    num, s1, s2 = [int(line.split(' ')[i]) for i in [1, 3, 5]]
    buffer = stacks[s1-1][:num]
    if num == len(stacks[s1-1]):
        stacks[s1-1] = ''
    else:
        stacks[s1-1] = stacks[s1-1][num:]
    stacks[s2 - 1] = buffer + stacks[s2 - 1]
    # stacks[s2-1] = buffer[::-1]+stacks[s2-1]

ar = []
for i in range(0, len(stacks)):
    ar.append(stacks[i][0])

print(''.join(ar))