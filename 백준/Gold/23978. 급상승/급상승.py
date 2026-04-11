from sys import stdin
input = stdin.readline

def boj23978():
    import math
    
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    d = [A[i+1] - A[i] for i in range(N-1)]
    d.sort()
    
    ps = [0]*(N)
    ps2 = [0]*(N)
    
    for i in range(N-1):
        ps[i+1] = ps[i] + d[i]
        ps2[i+1] = ps2[i] + d[i]*d[i]
    
    ans = 10**18
    
    for k in range(N):
        S = ps[k]
        S2 = ps2[k]
        
        a = (N - k)
        b = (N - k) + 2*S
        c = - (S2 - S) - 2*K
        D = b*b - 4*a*c
        if D < 0: continue
        
        X = (-b + int(math.isqrt(D))) // (2*a)
        
        while True:
            val = (N-k)*X*(X+1)//2 + X*S - (S2 - S)//2
            if val >= K: break
            X += 1
        
        if k == 0 or d[k-1] <= X:
            if k == N-1 or X < d[k]:
                ans = min(ans, X)
    
    print(ans)


if __name__ == "__main__": boj23978()