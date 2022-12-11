file = open('C:/Users/Rafist0/Documents/adventOfCode2022/programs/data/02.12.input.txt').readlines()

# POINTS
# WIN = 6
# DRAW = 3
# LOSE = 0

# OPONNENT
# A for Rock
# B for Paper
# C for Scissors

# ME
# X for Rock = 1
# Y for Paper = 2
# Z for Scissors = 3

# Problem One

options = {
    "A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 0 + 3,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 6 + 1,
    "C Y": 0 + 2,
    "C Z": 3 + 3
}

score = 0
for i, line in enumerate(file):
    if i != len(file) - 1:
        line = line[:-1]
    score += options[line]

print(f"Problem One :: {score}")

# Problem Two

# A Rock
# B Paper
# C Scissors

# X lose
# Y draw
# Z win

options = {
    "A X": 0 + 3,
    "A Y": 3 + 1,
    "A Z": 6 + 2,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 0 + 2,
    "C Y": 3 + 3,
    "C Z": 6 + 1
}

score = 0
for i, line in enumerate(file):
    if i != len(file) - 1:
        line = line[:-1]
    score += options[line]

print(f"Problem Two :: {score}")
