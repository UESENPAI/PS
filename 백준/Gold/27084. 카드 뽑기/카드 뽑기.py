from sys import stdin
input = stdin.readline

def boj27084():
    from collections import Counter

    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7

    cnt = Counter(A)
    ans = 1
    for f in cnt.values(): 
        ans *= (f + 1) 
        ans %= MOD

    print((ans - 1) % MOD)

if __name__ == '__main__': boj27084()