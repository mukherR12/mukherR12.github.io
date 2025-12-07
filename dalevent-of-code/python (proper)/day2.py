import re
from tqdm import tqdm

def makechunks(string, length):
    out = []
    for i in range(0, len(string), length):
        out.append(string[i:length+i])
    return out

def all_equal(list):
    if list != [list[0]]*len(list):
        return False
    return True

with open("inputs/day2.txt", "r") as file:
    line = file.readlines()[0]
    line = line.strip()

line = re.split(",", line)

invalids = []

for idrange in line:
    minid = int(idrange.split("-")[0])
    maxid = int(idrange.split("-")[1])
    for id in tqdm(range(minid, maxid+1, 1)):
        Valid = True
        for i in (range(1, (len(str(id))//2)+1)):
            chunks = makechunks(str(id), i)
            if all_equal(chunks) and Valid == True:
                invalids.append(id)
                Valid = False

print(sum(invalids))