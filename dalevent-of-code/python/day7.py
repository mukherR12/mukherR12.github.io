from pyscript import document #type: ignore
from pyodide.ffi import create_proxy #type: ignore

def run(event):
    inp = document.getElementById("day7-box").value
    lines = inp.splitlines()
    matrix = [list(line.strip()) for line in lines]


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
    document.getElementById("day7-out-1").textContent = str(splits)
    document.getElementById("day7-out-2").textContent = str(total_timelines)

run_proxy = create_proxy(run)
document.getElementById("day7-btn").addEventListener("click", run_proxy)

                