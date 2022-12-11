file = open(
    "C:/Users/Rafist0/Documents/adventOfCode2022/programs/data/8.12.input.txt").read().split('\n')
file = [[int(c) for c in a] for a in file]

mx = len(file)
my = len(file[0])

visible = []
for x in range(mx):
    # row left
    a = -1
    for y in range(my):
        if file[x][y] > a:
            a = file[x][y]
            visible.append((x, y))
    # row right
    a = -1
    for y in reversed(range(my)):
        if file[x][y] > a:
            a = file[x][y]
            visible.append((x, y))

for y in range(my):
    # column top
    a = -1
    for x in range(mx):
        if file[x][y] > a:
            a = file[x][y]
            visible.append((x, y))
    # column bottom
    a = -1
    for x in reversed(range(mx)):
        if file[x][y] > a:
            a = file[x][y]
            visible.append((x, y))

print(len(set(visible)))

hi = 0
for x in range(mx):
    for y in range(my):
        # top
        st = 0
        for tx in reversed(range(x)):
            if file[x][y] > file[tx][y]:
                st += 1
            else:
                st += 1
                break
        # bottom
        sb = 0
        for tx in range(x, mx):
            if tx != x:
                if file[x][y] > file[tx][y]:
                    sb += 1
                else:
                    sb += 1
                    break
        # left
        sl = 0
        for ty in reversed(range(y)):
            if ty != y:
                if file[x][y] > file[x][ty]:
                    sl += 1
                else:
                    sl += 1
                    break
        # right
        sr = 0
        for ty in range(y, my):
            if ty != y:
                if file[x][y] > file[x][ty]:
                    sr += 1
                else:
                    sr += 1
                    break
        scenic = st * sb * sl * sr
        if scenic > hi:
            hi = scenic

print(hi)
