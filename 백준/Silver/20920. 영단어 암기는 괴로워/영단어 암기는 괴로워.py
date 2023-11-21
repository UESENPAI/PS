import sys

N, M = map(int,sys.stdin.readline().strip().split())

myvoca = dict()

for _ in range(N):
    voc = sys.stdin.readline().strip()
    if(len(voc) > M-1):
        if voc in myvoca: myvoca[voc] += 1
        else: myvoca[voc] = 1

myvoca = sorted(myvoca.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for items in myvoca: print(items[0])