import sys
from math import gcd

N = int(sys.stdin.readline().strip())

rngarr = []
rngarr=list(map(int,sys.stdin.readline().split()))

for i in range(1,N):
    mdv = gcd(rngarr[0], rngarr[i])
    print(f'{rngarr[0]//mdv}/{rngarr[i]//mdv}')