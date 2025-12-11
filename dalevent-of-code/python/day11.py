import pyodide_js
await pyodide_js.loadPackage('micropip')
import micropip
await micropip.install("networkx") #type: ignore

import networkx as nx
from functools import cache
from pyscript import document #type: ignore
from pyodide.ffi import create_proxy #type: ignore

def run(event):
    inp = document.getElementById("day11-box").value
    lines = {line.split(":")[0]: line.split(":")[1].split() for line in inp.splitlines()}
    
    @cache
    def count(node, dac=0, fft=0):
        if node == 'out': 
            return dac and fft
        elif node == 'dac': 
            dac = True
        elif node == 'fft':
            fft = True
        return sum(count(next, dac, fft) for next in lines[node])
    
    G = nx.DiGraph()
    for s in lines:
        targets = lines[s]
        for t in targets:
            G.add_edge(s, t)

    paths = nx.all_simple_paths(G, source="you", target="out")

    document.getElementById("day11-out-1").textContent = str(len(list(paths)))
    document.getElementById("day11-out-2").textContent = str(count('svr'))

run_proxy = create_proxy(run)
document.getElementById("day11-btn").addEventListener("click", run_proxy)