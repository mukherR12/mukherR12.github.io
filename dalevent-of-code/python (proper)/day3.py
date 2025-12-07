from tqdm import tqdm
import math

with open("inputs/day3.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

count = 0

for _, line in tqdm(enumerate(lines)):
    bank = list(line)
    bank = [int(cell) for cell in bank]
    maxes = []
    marker = 0
    for i in range(-11, 0):
        maxi = max(bank[marker:i])
        maxes.append(maxi)
        marker += bank[marker:i].index(maxi) + 1    
    maxes.append(max(bank[marker:])) 
    count += (int("".join([str(cell) for cell in maxes])))

print(count)
    
