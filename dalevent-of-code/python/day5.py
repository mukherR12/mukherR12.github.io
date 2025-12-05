from pyscript import document #type: ignore
from pyodide.ffi import create_proxy #type: ignore

freshranges = []

def run(event):
    inp = document.getElementById("day5-box").value
    lines = inp.splitlines()
    lines = [line.strip() for line in lines]
        
    for idrange in (lines[:lines.index("")]):
        minid = int(idrange.split("-")[0])
        maxid = int(idrange.split("-")[1])
        freshranges.append([minid, maxid])

    def day5(part):
        count = 0
        ##part 1
        if part == 1:
            for id in (lines[lines.index("")+1:]):
                for freshrange in freshranges:
                    if freshrange[0] <= int(id) <= freshrange[1]:
                        count += 1
                        break
        ##part 2
        elif part == 2:
            freshranges.sort(key= lambda x: (x[0], x[1]))

            lastmax = 0

            for freshrange in freshranges:
                if freshrange[0] > lastmax:
                    count += (freshrange[1] - freshrange[0] + 1)
                else:
                    if ((freshrange[1] - freshrange[0] + 1) - (lastmax-freshrange[0]+1)) > 0:
                        count += ((freshrange[1] - freshrange[0] + 1) - (lastmax-freshrange[0]+1))
                lastmax = freshrange[1]
        return (count)
    
    document.getElementById("day5-out-1").textContent = str(day5(1))
    document.getElementById("day5-out-2").textContent = str(day5(2))
    
run_proxy = create_proxy(run)
document.getElementById("day5-btn").addEventListener("click", run_proxy)