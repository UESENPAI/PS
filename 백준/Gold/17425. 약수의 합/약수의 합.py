import sys
input = sys.stdin.readline

def boj17425():
    T = int(input().strip())
    
    f, g = [0] * 1000001, [0] * 1000001
    
    for n in range(1, 1000001):
        for nm in range(n, 1000001, n): f[nm] += n

    for n in range(1, 1000001): g[n] = g[n-1] + f[n]

    for _ in range(T):
        N = int(input().strip())
        print(g[N])

if __name__ == '__main__': boj17425()