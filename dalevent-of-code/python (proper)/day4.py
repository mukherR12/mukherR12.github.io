from tqdm import tqdm
import math

with open("./2025/inputs/day4.txt", "r") as file:
    lines = file.readlines()
    lines = [list(line.strip()) for line in lines]
directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]
count = float("inf")
sum = 0
while count > 0:
    count = 0
    for a, line in tqdm(enumerate(lines)):
        for b, char in enumerate(line):
            if lines[a][b] == "@":
                rolls = 0
                for direction in directions:
                    try: 
                        if a+direction[0] >= 0 and b+direction[1] >= 0 and lines[a+direction[0]][b+direction[1]] == "@":
                            rolls += 1
                    except IndexError:
                        pass
                if rolls < 4:
                    count += 1
                    lines[a][b] = "x"
    sum += count
print(sum)