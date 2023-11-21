import sys
from math import sqrt

N = int(sys.stdin.readline().strip())

if N==1:
    print(1)
    exit()

cnt = 0
end = int(sqrt(N)) + 2
for n in range(1, end):
    if n*n<N: cnt+=1 

print(cnt)
