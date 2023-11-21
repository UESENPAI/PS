import sys

N = int(sys.stdin.readline())
if N>100: raise Exception(f'INPUT ERROR!')

M = [[0 for col in range(101)] for row in range(101)]

for _ in range(N):
    X, Y = list(map(int, sys.stdin.readline().split()))
    for i in range(10):
        for j in range(10):
            M[X+i][Y+j]=1

sum = 0
for i in range(101):
    for j in range(101):
        if M[i][j]: sum = sum + 1

print(f'{sum}')