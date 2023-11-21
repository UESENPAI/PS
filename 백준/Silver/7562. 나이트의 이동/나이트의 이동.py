import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(4444)

T = int(input().strip())

def BFS(x, y, fx, fy, l):
    CB = [[0 for _ in range(l)] for _ in range(l)]
    q = deque([[x,y]])

    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    while q:
        p = q.popleft()
        if p[0]==fx and p[1]==fy: break
        for i in range(8):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if 0<=nx<l and 0<=ny<l:
                if not CB[nx][ny]:
                    CB[nx][ny] = CB[p[0]][p[1]] + 1
                    q.append([nx, ny])

    return CB[fx][fy]


for _ in range(T):
    l = int(input().strip())
    x, y = map(int, input().strip().split())
    fx, fy = map(int, input().strip().split())
    
    print(BFS(x, y, fx, fy, l))
