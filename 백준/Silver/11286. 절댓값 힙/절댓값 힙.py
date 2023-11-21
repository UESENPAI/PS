import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())

X = []
for _ in range(N):
    x = int(input().strip())
    if x: heapq.heappush(X, (abs(x), x))
    else:
        if len(X): print(heapq.heappop(X)[1])
        else: print(0)
