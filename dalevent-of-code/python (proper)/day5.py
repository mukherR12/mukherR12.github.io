from collections import deque;
from tqdm import tqdm

freshranges = []

with open("inputs/day5.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    
for idrange in tqdm(lines[:lines.index("")]):
    minid = int(idrange.split("-")[0])
    maxid = int(idrange.split("-")[1])
    freshranges.append([minid, maxid])

count = 0

##part 1
# for id in tqdm(lines[lines.index("")+1:]):
#     for freshrange in freshranges:
#         if freshrange[0] <= int(id) <= freshrange[1]:
#             count += 1
#             break

##part 2

freshranges.sort(key= lambda x: (x[0], x[1]))

lastmax = 0

for freshrange in freshranges:
    count += ((freshrange[1] - freshrange[0] + 1) if freshrange[0] > lastmax else (freshrange[1] - lastmax) if freshrange[1] > lastmax else 0)
    lastmax = freshrange[1]
print(count)

###JS
# const freshranges = document.getElementsByTagName("pre")[0].innerText.split("\n").slice(0, document.getElementsByTagName("pre")[0].innerText.split("\n").indexOf("")).map(x => x.split("-").map(n => Number(n))).sort((a,b) => a[0] - b[0] || a[1] - b[1]);
# let count = 0
# let lastmax = 0
# for (const freshrange in freshranges) {
#     console.log(freshrange)
#     count = count + ((freshrange[0] > lastmax) ? (freshrange[1] - freshrange[0] + 1) : ((freshrange[1] > lastmax) ? (freshrange[1] - lastmax) : 0))
#     lastmax = freshrange[1]
# }
# console.log(count)