import sys
from math import gcd
input = sys.stdin.readline

def boj14476():
    N = int(input().strip())
    nums = list(map(int, input().strip().split()))

    if N < 4: print(-1)
    else:
        mgcd, rnum = -1, -1
        pgcd, sgcd = [0]*N, [0]*N

        pgcd[0] = nums[0]
        for i in range(1, N): pgcd[i] = gcd(pgcd[i-1], nums[i])

        sgcd[N-1] = nums[N-1]
        for i in range(N-2, -1, -1): sgcd[i] = gcd(sgcd[i+1], nums[i])

        for i in range(N):
            if not i: cgcd = sgcd[1]
            elif i == N-1: cgcd = pgcd[N-2]
            else: cgcd = gcd(pgcd[i-1], sgcd[i+1])
            if nums[i]%cgcd:
                if cgcd > mgcd: mgcd, rnum = cgcd, nums[i]

        print(-1) if mgcd == -1 else print(mgcd, rnum)     

if __name__ == '__main__': boj14476()