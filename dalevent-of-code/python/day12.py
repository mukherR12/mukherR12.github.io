from pyscript import document #type: ignore
from pyodide.ffi import create_proxy #type: ignore

def run(event):
    document.getElementById("day12-out-1").textContent = str(sum([(int(r.split(":")[0].split("x")[0].strip())*int(r.split(":")[0].split("x")[1].strip())>= 9*sum([int(n) for n in r.split(":")[1].split()])) for r in document.getElementById("day12-box").value.splitlines()[31:]]))
    document.getElementById("day12-out-2").textContent = "Merry Christmas!"

run_proxy = create_proxy(run)
document.getElementById("day12-btn").addEventListener("click", run_proxy)