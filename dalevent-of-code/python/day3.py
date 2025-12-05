from pyscript import document
from pyodide.ffi import create_proxy

def run(event):
    raw_input = document.getElementById("day3-box").value
    lines = raw_input.splitlines()
    lines = [line.strip() for line in lines]

    def day3(part):
        count = 0
        for _, line in (enumerate(lines)):
            bank = list(line)
            bank = [int(cell) for cell in bank]
            maxes = []
            marker = 0
            for i in range(-(part-1), 0):
                maxi = max(bank[marker:i])
                maxes.append(maxi)
                marker += bank[marker:i].index(maxi) + 1    
            maxes.append(max(bank[marker:])) 
            count += (int("".join([str(cell) for cell in maxes])))
        return count
    document.getElementById("day3-out-1").textContent = str(day3(2))

    document.getElementById("day3-out-2").textContent = str(day3(12))
    
run_proxy = create_proxy(run)
document.getElementById("day3-btn").addEventListener("click", run_proxy)