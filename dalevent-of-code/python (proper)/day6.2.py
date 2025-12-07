import math
import re

with open("inputs/day6.txt", "r") as file: lines = file.readlines()

numbers, pointer, vals, su = [("".join([line[i] for line in lines[:-1]])) for i in range(len(lines[:-1][0]))], 0, [], 0

for num in numbers:
    if num.strip() == "":
        if lines[-1].strip().split()[pointer] == "*":
            su += math.prod(vals)
        else: su += sum(vals)
        pointer += 1
        vals = []
        continue
    else:
        n = int(num)
        vals.append(n)
print(su)