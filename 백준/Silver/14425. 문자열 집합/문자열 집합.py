import sys

N, M = map(int,sys.stdin.readline().split())

S = set()
for s in range(N):
    S.add(sys.stdin.readline())

chk = set()
cnt = 0
for c in range(M):
    cstr = (sys.stdin.readline())
    if cstr in S:
        cnt = cnt + 1

print(f'{cnt}')