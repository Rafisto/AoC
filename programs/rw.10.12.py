import numpy

file = open("C:/Users/Rafist0/Documents/adventOfCode2022/programs/data/10.12.input.txt").read().split('\n')

sprite = ['.' for x in range(240)]
total = 0
EXEC = 0
X = 1


def EvalExec(cycle, register):
    if cycle % 40 == 20:
        return register * cycle
    return 0


def DrawPixel(cycle, register):
    if cycle < 40:
        print(f'c{cycle}:r{register}')
    if cycle % 40 == register - 1:
        sprite[cycle] = "#"
    elif cycle % 40 == register:
        sprite[cycle] = "#"
    elif cycle % 40 == register + 1:
        sprite[cycle] = "#"


DrawPixel(0, 0)
for line in file:
    DrawPixel(EXEC, X)
    if line == "noop":
        EXEC += 1
        DrawPixel(EXEC, X)
        total += EvalExec(EXEC, X)
        continue
    line = line.split(" ")
    if line[0] == "addx":
        EXEC += 1
        total += EvalExec(EXEC, X)
        DrawPixel(EXEC, X)
        EXEC += 1
        X += int(line[1])
        total += EvalExec(EXEC, X)
        DrawPixel(EXEC, X)

print(total)

print(sprite)
for i in range(6):
    print(''.join(sprite)[40 * i:40 * i + 40])
