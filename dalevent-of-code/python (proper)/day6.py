import math

with open("inputs/day6.txt", "r") as file:
    lines = file.readlines()
    nums = [[int(num) for num in line.strip().split()] for line in lines[:-1]]
    ops = lines[-1].strip().split()

gt = 0

for a in range(len(nums[0])):
    tot = []
    for num in nums:
        tot.append(num[a])
    print(tot)
    if ops[a] == "*":
        gt += math.prod(tot)
    else: gt += sum(tot)

print(gt)