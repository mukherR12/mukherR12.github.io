import re
from pyscript import document
from pyodide.ffi import create_proxy

def makechunks(string, length):
    out = []
    for i in range(0, len(string), length):
        out.append(string[i:length+i])
    return out

def all_equal(list):
    if list != [list[0]]*len(list):
        return False
    return True

def run(event):
    raw_input = document.getElementById("day2-box").value
    line = raw_input.strip()

    line = re.split(",", line)

    invalids = []

    for idrange in line:
        minid = int(idrange.split("-")[0])
        maxid = int(idrange.split("-")[1])
        for id in (range(minid, maxid+1, 1)):
            Valid = True
            for i in (range(1, (len(str(id))//2)+1)):
                chunks = makechunks(str(id), i)
                if all_equal(chunks) and Valid == True:
                    invalids.append(id)
                    Valid = False
    value = sum(invalids)
    document.getElementById("day2-out").textContent = str(value)

run_proxy = create_proxy(run)
document.getElementById("day2-btn").addEventListener("click", run_proxy)