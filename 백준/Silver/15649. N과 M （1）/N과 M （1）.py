import sys
from itertools import permutations

N, M = map(int,sys.stdin.readline().split())

narr = list(range(1,N+1))

ans = list(permutations(narr, M))

for i in ans: print(' '.join(map(str,i)))