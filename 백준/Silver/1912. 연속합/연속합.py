import sys

N = int(sys.stdin.readline().strip())

arr = list(map(int, sys.stdin.readline().strip().split()))

sarr = [arr[0]]
for i in range(N-1):
    sarr.append(max(sarr[i]+arr[i+1],arr[i+1]))
print(f'{max(sarr)}')
