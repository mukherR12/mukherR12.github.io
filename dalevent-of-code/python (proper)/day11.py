from collections import deque
import networkx as nx
from functools import cache

with open("inputs/day11.txt", "r") as file:
    lines = {line.split(":")[0]: line.split(":")[1].split() for line in file.readlines()}
print(lines)
G = nx.DiGraph()

@cache
def count(node, dac=0, fft=0):
    if node == 'out': 
        return dac and fft
    elif node == 'dac': 
        dac = True
    elif node == 'fft':
        fft = True
    return sum(count(next, dac, fft) for next in lines[node])

for s in lines:
    targets = lines[s]
    for t in targets:
        G.add_edge(s, t)


paths = nx.all_simple_paths(G, source="you", target="out")
print(len(list(paths)))


print(count('svr'))