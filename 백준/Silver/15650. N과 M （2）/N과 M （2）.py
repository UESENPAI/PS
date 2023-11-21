import sys
from itertools import combinations

N, M = map(int,sys.stdin.readline().split())

narr = list(range(1,N+1))

ans = list(combinations(narr, M))

for i in ans: print(' '.join(map(str,i)))
