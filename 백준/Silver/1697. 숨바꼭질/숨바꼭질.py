import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(666) 

def BFS(N, K):
    space = [0 for _ in range(100001)]
    q = deque([N])
    while q:
        p = q.popleft()
        if p==K: break
        for n in (p-1, p+1, 2*p):
            if 0<=n<100001 and not space[n]:
                space[n] = space[p] + 1
                q.append(n)
    return space[K]

N, K = map(int, input().strip().split())
    
print(BFS(N,K))