import sys

A, B = [], []

N, M = map(int, sys.stdin.readline().split())

for row in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    A.append(row)

for row in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    B.append(row)
    
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()