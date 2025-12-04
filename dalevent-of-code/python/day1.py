from pyscript import document
from pyodide.ffi import create_proxy

def run_code():
    raw_input = document.getElementById("day1-box").value
    lines = raw_input.strip().splitlines()

    signs = {"L": -1, "R": 1}
    dial_position = 50
    zeros_encountered = 0

    for line in lines:
        direction = line[0]
        turns = int(line[1:])
        sign = signs[direction]

        for _ in range(turns):
            dial_position += sign
            if dial_position == 100:
                dial_position = 0
            if dial_position == -1:
                dial_position = 99
            if dial_position == 0:
                zeros_encountered += 1

    document.getElementById("day1-out").textContent = str(zeros_encountered)


run_code_proxy = create_proxy(run_code)
document.getElementById("day1-btn").addEventListener("click", run_code_proxy)