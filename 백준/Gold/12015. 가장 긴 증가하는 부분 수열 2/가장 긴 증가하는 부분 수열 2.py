import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().strip().split()))

LIS = [A[0]]

for a in A:
    if LIS[-1] < a: LIS.append(a)
    else: LIS[bisect_left(LIS,a)] = a

print(len(LIS))