import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(666) 


N, M = map(int, input().strip().split())
    
mat = [list(map(int, input().strip())) for _ in range(N)]

def BFS(x, y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if mat[nx][ny]==1:
                    mat[nx][ny] = mat[x][y] + 1
                    que.append((nx, ny))
                else: continue
            else: continue
                
    return mat[N-1][M-1]

print(BFS(0, 0))