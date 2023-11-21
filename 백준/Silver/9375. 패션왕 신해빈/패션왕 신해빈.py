import sys
from collections import Counter

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    closet = list()
    for _ in range(n):
        _, B = map(str, sys.stdin.readline().split())
        closet.append(B)

    cdict = Counter(closet)

    cs = 1
    for key in cdict:
        cs *= (cdict[key]+1)

    print(cs-1)