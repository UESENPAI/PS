import sys

N, K = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

result = []
result.append(sum(arr[:K]))

for i in range(N - K):
    result.append(result[i] - arr[i] + arr[K+i])
        
print(max(result))
