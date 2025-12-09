from pyscript import document #type: ignore
from pyodide.ffi import create_proxy #type: ignore
from itertools import combinations

def euclidian_distance(c1, c2):
    return ((c2[0]-c1[0])**2 + (c2[1]-c1[1])**2 + (c2[2] - c1[2])**2)

def nested_index(target, list):
    for a in range(len(list)):
        for b in range(len(list[a])):
            if list[a][b] == target:
                return a
    return -1

def run(event):
    inp = document.getElementById("day8-box").value
    lines = [[int(num) for num in line.strip().split(",")] for line in inp.splitlines()]

    combs = ((list(combinations(lines, 2))))

    combs.sort(key = lambda x: euclidian_distance(x[0], x[1]))

    circuits = [[c] for c in lines]

    for p1, p2 in combs[:1000]:
        x1 = nested_index(p1, circuits)
        x2 = nested_index(p2, circuits)
        if x1 != x2:
            circuits[x1].extend(circuits[x2])
            circuits.pop(x2)

    sizes = sorted([len(c) for c in circuits], reverse=True)
    document.getElementById("day8-out-1").textContent = str(sizes[0] * sizes[1] * sizes[2])

run_proxy = create_proxy(run)
document.getElementById("day8-btn").addEventListener("click", run_proxy)
