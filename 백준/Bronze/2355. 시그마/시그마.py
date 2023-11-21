import sys

A, B = map(int,sys.stdin.readline().strip().split())

alpha, omega = min(A, B), max(A, B)

n = omega - alpha

ans = int(alpha*(n+1) + n*(n+1)/2)

print(ans)
