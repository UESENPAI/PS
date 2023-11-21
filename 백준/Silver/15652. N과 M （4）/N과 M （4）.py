import sys
from itertools import combinations_with_replacement as cwr

N, M = map(int,sys.stdin.readline().split())

narr = list(range(1,N+1))

ans = list(cwr(narr, M))

for i in ans: print(' '.join(map(str,i)))