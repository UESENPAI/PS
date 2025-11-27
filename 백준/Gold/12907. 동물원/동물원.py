from sys import stdin
input = stdin.readline

def boj12907():
    N = int(input())
    arr = list(map(int, input().split()))
    
    from collections import Counter
    from math import comb

    arr.sort()
    count = Counter(arr)
    ans = 0

    for K_r in range(N+1):
        K_c = N - K_r
        valid = True
        ways = 1
        for v in count:
            need = (v < K_r) + (v < K_c)
            if need != count[v]:
                valid = False
                break
            ways *= comb(count[v], (v < K_r))
        if valid: ans += ways
    print(ans)

if __name__ == "__main__": boj12907()