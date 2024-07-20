from sys import stdin
from math import isqrt
input = stdin.readline

def boj1612():
    N = int(input().strip())
    hnums=[]
    dic=dict()
    for _ in range(N):
        hnums.append(int(input().strip()))
        dic[hnums[-1]] = dic.get(hnums[-1], 0) + 1
    ans = [0] * N
    for key, hnum in enumerate(hnums):
        for factor in range(1, isqrt(hnum) + 1):
            if not hnum % factor:
                ans[key] += (dic.get(factor, 0) - (hnum//factor == hnum) if factor != hnum//factor else 0) + dic.get(hnum//factor, 0) - (factor == hnum)
    for _ in range(N): print(ans[_])
    
if __name__ == '__main__': boj1612()