import pyodide_js
await pyodide_js.loadPackage('micropip')
import micropip
await micropip.install("scipy") #type: ignore

from collections import deque
from scipy.optimize import linprog
from pyscript import document #type: ignore
from pyodide.ffi import create_proxy #type: ignore

def bfs_buttons(buttons, start, end):
    queue = deque([(tuple(start), 0)])
    visited = {tuple(start)}

    while queue:
        state, counter = queue.popleft()
        
        if list(state) == end:
            return counter
        
        for n in buttons:
            newstate = list(state)
            
            for index in n:
                newstate[index] = (newstate[index] + 1) % 2
                
            newstate_tuple = tuple(newstate)
            if newstate_tuple not in visited:
                visited.add(newstate_tuple)
                queue.append((newstate_tuple, counter + 1))
    return 0
    

def run(event):
    sum_lights = 0
    sum_joltages = 0
    inp = document.getElementById("day10-box").value
    lines = [line.split() for line in inp.splitlines()]
    
    for line in (lines):
        required = line[0][1:-1]
        lights = [0 if c == "." else 1 for c in required]
        
        buttons = [[int(c) for c in char[1:-1].split(",")] for char in line[1:-1]]
        joltages = [int(c) for c in line[-1][1:-1].split(",")]
    
        sum_lights += bfs_buttons(buttons, [0]*len(lights), lights)
    
        cost = [1] * len(buttons)
        num_targets = len(joltages)
        
        A_eq_matrix = [[1 if row_idx in button else 0 for button in buttons] for row_idx in range(num_targets)]
        sum_joltages += linprog(cost, A_eq=A_eq_matrix, b_eq=joltages, integrality=1).fun
        document.getElementById("day10-out-1").textContent = str(sum_lights)
        document.getElementById("day10-out-2").textContent = str(int(sum_joltages))

run_proxy = create_proxy(run)
document.getElementById("day10-btn").addEventListener("click", run_proxy)