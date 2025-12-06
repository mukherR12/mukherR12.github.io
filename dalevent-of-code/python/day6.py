import math
from pyscript import document #type: ignore
from pyodide.ffi import create_proxy #type: ignore

def run(event):
    inp = document.getElementById("day6-box").value
    lines = inp.splitlines()

    def day6(part):
        nums = [[int(num) for num in line.strip().split()] for line in lines[:-1]]
        ops = lines[-1].strip().split()
        numbers, pointer, vals, su = [("".join([line[i] for line in lines[:-1]])) for i in range(len(lines[:-1][0]))], 0, [], 0
        numbers.append("\n")
        gt = 0
        if part == 1:
            for a in range(len(nums[0])):
                tot = []
                for num in nums:
                    tot.append(num[a])
                print(tot)
                if ops[a] == "*":
                    gt += math.prod(tot)
                else: gt += sum(tot)
            return gt
        else:
            for num in numbers:
                if num.strip() == "":
                    if lines[-1].strip().split()[pointer] == "*":
                        su += math.prod(vals)
                    else: su += sum(vals)
                    pointer += 1
                    vals = []
                    continue
                else:
                    n = int(num)
                    vals.append(n)
            return (su)
    document.getElementById("day6-out-1").textContent = str(day6(1))
    document.getElementById("day6-out-2").textContent = str(day6(2))
    
run_proxy = create_proxy(run)
document.getElementById("day6-btn").addEventListener("click", run_proxy)