from sys import stdin
input = stdin.readline

def boj1286():
    from collections import defaultdict

    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]
    count = defaultdict(int)
    
    for i in range(N<<1):
        for j in range(M<<1):
            c = grid[i % N][j % M]
            count[c] += (i+1)*(j+1)*((N<<1)-i)*((M<<1)-j)
    
    print(*[count[ch] for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"], sep='\n')

if __name__ == '__main__': boj1286()