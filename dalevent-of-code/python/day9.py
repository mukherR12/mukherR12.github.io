from itertools import combinations
from pyscript import document #type: ignore
from pyodide.ffi import create_proxy #type: ignore

###part1
def area_formula(pos1, pos2):
    return (abs(pos1[0]-pos2[0])+1)*(abs(pos1[1]-pos2[1])+1)

def run(event):
    inp = document.getElementById("day9-box").value
    points = [[int(n) for n in line.split(",")] for line in inp.splitlines()]

    combos=list(combinations(points, 2))
    combos.sort(key= lambda x: area_formula(x[0], x[1]), reverse=True)

    ##part2 aaaaaaaaaaaaaaaa
    area = 0
    for x1, y1 in points:
        for x2, y2 in points:
            box_x1, box_x2 = min(x1, x2), max(x1, x2) 
            box_y1, box_y2 = min(y1, y2), max(y1, y2)
            for i, (bounds_x1, bounds_y1) in enumerate(points): #side start coords
                bounds_x2, bounds_y2 = points[(i+1) % len(points)] #side end coords
                if (max(bounds_x1, bounds_x2) > box_x1 and box_x2 > min(bounds_x1, bounds_x2) and max(bounds_y1, bounds_y2) > box_y1 and box_y2 > min(bounds_y1, bounds_y2)):
                    break
            else:
                area = max(area, area_formula([box_x1, box_y1], [box_x2, box_y2]))
                
    document.getElementById("day9-out-1").textContent = str(area_formula(combos[0][0], combos[0][1]))
    document.getElementById("day9-out-2").textContent = str(area)

run_proxy = create_proxy(run)
document.getElementById("day9-btn").addEventListener("click", run_proxy)