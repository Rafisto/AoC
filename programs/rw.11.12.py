import math
import numpy

file = open("C:/Users/Rafist0/Documents/adventOfCode2022/programs/data/11.12.input.txt").read().split('\n\n')

monkeys = []


class Monkey(object):
    def __init__(self, starting_items, operation, test, p_true, p_false):
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.p_true = p_true
        self.p_false = p_false
        self.inspects = 0

    def EvalItems(self):
        items = self.starting_items.copy()
        for starting_item in self.starting_items:
            # print(f"Checking {starting_item}")
            self.inspects += 1
            if part == "two":
                val = eval(self.operation, {"old": starting_item})
                val = val % mod
                if val % self.test == 0:
                    items.remove(starting_item)
                    monkeys[self.p_true].AddItem(val)
                else:
                    items.remove(starting_item)
                    monkeys[self.p_false].AddItem(val)
            else:
                val = math.floor(eval(self.operation, {"old": starting_item}) / 3)
                if val % self.test == 0:
                    items.remove(starting_item)
                    monkeys[self.p_true].AddItem(val)
                    # print(f"Gave {starting_item} to {self.p_true}")
                    # print(self.starting_items)
                else:
                    items.remove(starting_item)
                    monkeys[self.p_false].AddItem(val)
                    # print(f"Gave {starting_item} to {self.p_false}")
                    # print(self.starting_items)
        self.starting_items = items

    def AddItem(self, item):
        self.starting_items.append(item)


for monkey in file:
    monkey = monkey.split('\n')
    monkeys.append(Monkey([int(k) for k in monkey[1].split(':')[1].split(',')],
                          monkey[2].split(':')[1].split('=')[1],
                          int(monkey[3].split(' by ')[1]),
                          int(monkey[4].split()[-1]),
                          int(monkey[5].split()[-1])))

rounds = 10000

part = "two"
mod = int(numpy.prod([monkey.test for monkey in monkeys]))

for i in range(rounds):
    print(f"Round {i}")
    for monkey in monkeys:
        # print("monkey")
        # print(monkey.starting_items)
        monkey.EvalItems()

for monkey in monkeys:
    print(monkey.inspects)

inspects = [monkey.inspects for monkey in monkeys]
inspects.sort(reverse=True)
print("Two best inspectors")
print(inspects[0] * inspects[1])
