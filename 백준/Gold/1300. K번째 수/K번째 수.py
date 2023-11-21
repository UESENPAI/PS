import sys
input = sys.stdin.readline

N, K = int(input().strip()), int(input().strip())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2
    
    cnt = sum(min(mid//i, N) for i in range(1, N+1))
    
    if cnt >= K: answer, end = mid, mid - 1
    else: start = mid + 1
print(answer)