from sys import stdin
input = stdin.readline

def boj1286():
    from collections import defaultdict

    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]
    count = defaultdict(int)
    
    for i in range(N):
        for j in range(M):
            c = grid[i][j]
            sigma = 0
            for k in range(2):
                for l in range(2):
                    ii, jj = i + k*N, j + l*M
                    sigma += (ii+1)*(jj+1)*((N<<1) - ii)*((M<<1) - jj)
            count[c] += sigma

    print(*[count[ch] for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"], sep='\n')

if __name__ == '__main__': boj1286()