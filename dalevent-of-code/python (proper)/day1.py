signs = {"L": -1, "R": 1}
with open("inputs/day1.txt", "r") as file:
    lines = file.readlines()
    
zeros_per_line = []

dial_position = 50
zeros_encountered = 0
for line in lines:
    direction = line[0]
    turns = int(line[1:])

    sign = signs[direction]

    new_zeros = 0
    for _ in range(turns):
        dial_position += sign

        # update dial position
        if dial_position == 100:
            dial_position = 0

        if dial_position == -1:
            dial_position = 99

        if dial_position == 0:
            new_zeros += 1

    zeros_encountered += new_zeros
    zeros_per_line.append(f"{new_zeros}\n")

print(zeros_encountered)