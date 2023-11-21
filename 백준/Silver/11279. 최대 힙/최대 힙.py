import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())

X = []
for _ in range(N):
    x = int(input().strip())
    if x: heapq.heappush(X, (-x))
    else:
        if len(X): print(-1*heapq.heappop(X))
        else: print(0)