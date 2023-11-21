import sys
from math import inf
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    K = int(input().strip())
    DP = [[0 for _ in range(K+1)] for _ in range(K+1)]
    X = [0] + list(map(int, input().strip().split()))
    csum = [sum(X[:i]) for i in range(1,len(X)+1)]
    arg = [[0 for _ in range(K+1)] for _ in range(K+1)]
    for i in range(1,K+1): arg[i-1][i] = i
    
    for d in range(2, K+1):
        for i in range(0, K+1):
            if i+d>K: break
            j = i + d
            DP[i][j] = inf
            for k in range(arg[i][j-1], arg[i+1][j]+1):
                v = DP[i][k]+DP[k][j]+csum[j]-csum[i]
                if DP[i][j] > v: DP[i][j], arg[i][j] = v, k

    print(DP[0][K])
