import sys
input = sys.stdin.readline
sys.setrecursionlimit(10001) 

T = int(input().strip())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def DFS(x,y):
    global mat, dx, dy
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M) and (0 <= ny < N):
            if mat[nx][ny]:
                mat[nx][ny] = False
                DFS(nx, ny)
    return

for _ in range(T):
    M, N, K = map(int, input().strip().split())
    
    mat = [[False for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        X, Y = map(int, input().strip().split())
        mat[X][Y] = True

    worm = 0
    for m in range(M):
        for n in range(N):
            if mat[m][n]:
                worm+=1
                DFS(m,n)
                
    print(worm)
