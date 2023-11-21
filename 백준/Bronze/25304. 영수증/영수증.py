import sys

X = int(sys.stdin.readline())
if X<1 or X>1000000000: raise Exception(f'Wrong Input')

N = int(sys.stdin.readline())
if N<1 or N>100: raise Exception(f'Wrong Input')

ab = [[0 for col in range(2)] for row in range(N)]
sum = 0

for i in range(N):
    ab[i-1][0], ab[i-1][1] = map(int, sys.stdin.readline().split())
    if ab[i-1][0]<1 or ab[i-1][0]>1000000: raise Exception(f'Wrong Input')
    if ab[i-1][1]<1 or ab[i-1][1]>10: raise Exception(f'Wrong Input')
    sum = sum + ab[i-1][0]*ab[i-1][1]

if sum==X:
    print(f'Yes')
else:
    print(f'No')
