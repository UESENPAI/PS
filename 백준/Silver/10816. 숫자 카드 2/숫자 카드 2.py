import sys
from collections import Counter

N = int(sys.stdin.readline().strip())

icard = list(map(int, sys.stdin.readline().split()))

icardcnt = Counter(icard)

M = int(sys.stdin.readline().strip())

mcard = list(map(int, sys.stdin.readline().split()))

for q in mcard:
    print(icardcnt[q], end = " ")