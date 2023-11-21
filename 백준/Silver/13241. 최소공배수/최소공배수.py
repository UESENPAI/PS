import sys

A, B = map(int, sys.stdin.readline().strip().split())
res = A*B

while B:
    if A > B:
        A, B = B, A
    B %= A

print(res//A)