
with open("inputs/day7.txt", "r") as file:
    matrix = file.readlines()
    matrix = [list(line.strip()) for line in matrix]


splits = 0
visited = []
timelines = [0] * (matrix[0].index("S")) + [1] + [0]*(len(matrix[0])-matrix[0].index("S")-1)

for row in range(len(matrix)-1):
    next_timeline = [0] * len(matrix[0])
    
    for col in range(len(matrix[0])):
        #if no paths currently, ignore
        if timelines[col] == 0:
            continue
        
        #if theres a splitter below
        if matrix[row+1][col] == '^':
            #############part1#############
            if (row+1, col+1) not in visited or (row+1, col-1) not in visited:
                visited.append((row+1, col+1))
                visited.append((row+1, col-1))
                splits += 1
            ##############part2############
            #if splitter, take paths and put them on left and right
            next_timeline[col-1] += timelines[col]
            next_timeline[col+1] += timelines[col]
        else:
            ###########part1##############
            visited.append((row+1, col))
            ##########part2###############
            next_timeline[col] += timelines[col]
    timelines = next_timeline
total_timelines = sum(timelines)
print(total_timelines, splits)

                