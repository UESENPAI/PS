import sys

N, K = map(int, sys.stdin.readline().strip().split())

div = {1, N}
for d in range(2, N//2 + 1):
    if not N%d:
        div.add(d)

try: print(sorted(list(div))[K-1])
except IndexError: print(0)