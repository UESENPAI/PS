import sys

string = list(sys.stdin.readline().strip())
q = int(sys.stdin.readline().strip())

csum = [[0 for _ in range(len(string))] for _ in range(26)]
for sidx in range(len(string)):
    if not sidx:
        csum[(ord(string[sidx])-97)][sidx] += 1
    else:
        for aidx in range(26): csum[aidx][sidx] = csum[aidx][sidx-1]
        csum[(ord(string[sidx])-97)][sidx]+=1
        
for _ in range(q):
    a, l, r = map(str, sys.stdin.readline().strip().split())
    a, l, r = (ord(a)-97), int(l), int(r)
    if not l: print(f'{csum[a][r]}')
    else: print(f'{csum[a][r]-csum[a][l-1]}')