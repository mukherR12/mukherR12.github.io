from pyscript import document
from pyodide.ffi import create_proxy
  
directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]
def run(event):
    inp = document.getElementById("day4-box").value
    lines = inp.splitlines()
    lines = [list(line.strip()) for line in lines]
    def day4(part):
        count = float("inf")
        sum = 0
        while count > 0:
            count = 0
            for a, line in (enumerate(lines)):
                for b, char in enumerate(line):
                    if lines[a][b] == "@":
                        rolls = 0
                        for direction in directions:
                            try: 
                                if a+direction[0] >= 0 and b+direction[1] >= 0 and lines[a+direction[0]][b+direction[1]] == "@":
                                    rolls += 1
                            except IndexError:
                                pass
                        if rolls < 4:
                            count += 1
                            if part == 2:
                                lines[a][b] = "x"
            if part == 1:
                return count
            sum += count
        return sum
    
    document.getElementById("day4-out-1").textContent = str(day4(1))
    document.getElementById("day4-out-2").textContent = str(day4(2))

run_proxy = create_proxy(run)
document.getElementById("day4-btn").addEventListener("click", run_proxy)