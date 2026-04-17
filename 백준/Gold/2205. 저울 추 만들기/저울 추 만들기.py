from sys import stdin
input = stdin.readline

def solve():
    n = int(input())
    ans = [0] * (n + 1)

    cur = n
    while cur > 0:
        p = 1
        while p <= cur: p <<= 1

        L = p - cur

        for x in range(L, cur + 1): ans[x] = p - x

        cur = L - 1

    for i in range(1, n + 1): print(ans[i])

if __name__ == "__main__": solve()