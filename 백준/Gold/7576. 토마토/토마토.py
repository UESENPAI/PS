import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(4444)

def BFS(TMT):
    global M, N
       
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    q = deque([])
    for n in range(N):
        for m in range(M):
            if TMT[n][m]>0: q.append([n,m])

    while q:
        p = q.popleft()
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if 0<=nx<N and 0<=ny<M and not TMT[nx][ny]:
                TMT[nx][ny] = TMT[p[0]][p[1]] + 1
                q.append([nx, ny])
                
    if any(0 in row for row in TMT): return -1

    res = max(*map(max, TMT))
    if res !=1: return res-1
    else: return 0


M, N = map(int, input().strip().split())

TMT = [list(map(int, input().strip().split())) for _ in range (N)]

print(BFS(TMT))