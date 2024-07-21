from sys import stdin
from math import isqrt
input = stdin.readline

def boj1612():
    N = int(input().strip())

    colors = [0] * (N+1)
    colors[1], ccnt = 1, 1
    
    for idx in range(2, N+1):
        if not colors[idx]:
            ccnt += 1
            curcolor = ccnt
            for mul in range(idx, N+1, idx):
                if not colors[mul]: colors[mul] = curcolor
    
    print(ccnt)
    print(" ".join(map(str, colors[1:])))
    
if __name__ == '__main__': boj1612()