import sys

N = int(sys.stdin.readline().strip())

rect = []

for _ in range(N):
    rect.append(list(map(int,sys.stdin.readline().strip().split())))

trect = list(zip(*rect))

ans = 0
if N != 1:
    up = [max(e) for e in trect]
    down = [min(e) for e in trect]
    ans = (up[0]-down[0])*(up[1]-down[1])
print(ans)
