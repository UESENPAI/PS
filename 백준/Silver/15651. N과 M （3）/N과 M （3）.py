import sys
from itertools import product

N, M = map(int,sys.stdin.readline().split())

narr = list(range(1,N+1))

ans = list(product(narr, repeat = M))

for i in ans: print(' '.join(map(str,i)))