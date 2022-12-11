import numpy as np

file = open("C:/Users/Rafist0/Documents/adventOfCode2022/programs/data/9.12.input.txt").read().split('\n')

H_options = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
H_pos = [0, 0]
T_pos = [0, 0]
T_positions = [(0, 0)]
for line in file:
    direction, amount = line.split()
    amount = int(amount)
    for i in range(amount):
        H_pos = [H_pos[0] + H_options[direction][0], H_pos[1] + H_options[direction][1]]
        X_dif, Y_dif = H_pos[0] - T_pos[0], H_pos[1] - T_pos[1]
        if (abs(X_dif) >= 2) or (abs(Y_dif) >= 2):
            T_pos = [T_pos[0] + np.sign(X_dif), T_pos[1] + np.sign(Y_dif)]

        T_positions.append((T_pos[0], T_pos[1]))

print(len(set(T_positions)))

rope = [[0, 0]] * 10
H_pos = [0, 0]
T_pos = [0, 0]
T_positions = [(0, 0)]
for line in file:
    direction, amount = line.split()
    amount = int(amount)
    for i in range(amount):
        H_pos = rope[0]
        rope[0] = [H_pos[0] + H_options[direction][0], H_pos[1] + H_options[direction][1]]
        for j in range(len(rope) - 1):
            H_pos = rope[j]
            T_pos = rope[j + 1]
            X_dif, Y_dif = H_pos[0] - T_pos[0], H_pos[1] - T_pos[1]
            if (abs(X_dif) >= 2) or (abs(Y_dif) >= 2):
                rope[j + 1] = [T_pos[0] + np.sign(X_dif), T_pos[1] + np.sign(Y_dif)]
        T_positions.append((rope[-1][0], rope[-1][1]))

print(len(set(T_positions)))
