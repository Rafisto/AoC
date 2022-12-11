file = open("C:/Users/Rafist0/Documents/adventOfCode2022/programs/data/4.12.input.txt").readlines()


def contains(xs, xm, ys, ym):
    return (xs <= ys and xm >= ym) or (ys <= xs and ym >= xm)


def overlaps(xs, xm, ys, ym):
    return (xs <= ys <= xm) or (ys <= xs <= ym)


contained = 0
overlapped = 0
for line in file:
    vals = line.replace('\n', '').split(',')
    xs, xm, ys, ym = [int(vals[i // 2].split('-')[i % 2]) for i in range(4)]
    if contains(xs, xm, ys, ym): contained += 1
    if overlaps(xs, xm, ys, ym): overlapped += 1

print(contained)
print(overlapped)

# int = 0-3

# 2 -> 0b10 - [2:] -> '10' -> '10'[0] '10'[1] -> 1, 0
# 2 -> [0] 2//2=1 ^ [1] 2%2=0

# 0, 0
# 0, 1
# 1, 0
# 1, 1
