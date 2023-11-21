import sys
input = sys.stdin.readline

N, C = map(int,input().strip().split())

X = sorted([int(input().strip()) for _ in range(N)])

alpha, omega = 1, X[-1]-X[0]

if C==2:
    print(omega)
    exit()

ans=0
while alpha < omega:
    mid = (alpha + omega) // 2

    cnt = 1
    tmp = X[0]
    for x in X:
        if x - tmp >= mid:
            cnt+=1
            tmp = x
            
    if cnt < C: omega = mid
    else: ans, alpha = mid, mid+1
        
print(ans)
