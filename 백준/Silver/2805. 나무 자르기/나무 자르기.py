import sys

N, M = map(int,sys.stdin.readline().strip().split())

T = list(map(int, sys.stdin.readline().strip().split()))

alpha, omega = 1, max(T)

while alpha <= omega:
    mid = (alpha + omega) // 2
    
    cut = sum([t - mid for t in T if t >= mid])
    
    if cut >= M: alpha = mid + 1
    else: omega = mid - 1
    
print(omega)