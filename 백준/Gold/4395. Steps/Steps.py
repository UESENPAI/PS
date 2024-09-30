import sys
from math import isqrt
input = sys.stdin.readline

def boj4395():
    n = int(input())
    tcs = [tuple(map(int, input().split())) for _ in range(n)]

    def getstep(x, y):
        d = y - x
        if not d: return 0
        step = isqrt(d)
        ans = step<<1
        if step * step == d: ans-=1
        else:
            Z = d - step * step
            if Z > step:ans += 1 
        return ans

    for x, y in tcs: print(getstep(x, y))

if __name__ == "__main__": boj4395()