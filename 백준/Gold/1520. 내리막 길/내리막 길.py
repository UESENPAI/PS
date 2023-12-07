import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def boj1520():
    M, N = map(int,input().strip().split())
    hmap = [list(map(int, input().strip().split())) for _ in range(M)]
    dp = [[-1 for _ in range(N)] for _ in range (M)]

    DIR = [(-1,0), (1,0), (0,-1), (0,1)]

    def dfs(x, y):
        if x == M-1 and y == N-1: return 1
        
        if dp[x][y] != -1: return dp[x][y]

        dp[x][y] = 0
        for dx, dy in DIR:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and hmap[nx][ny] < hmap[x][y]:
                dp[x][y] += dfs(nx, ny)

        return dp[x][y]

    print(dfs(0,0))
    
if __name__ == "__main__":
    boj1520()