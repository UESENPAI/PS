from sys import stdin
input = stdin.readline

def boj7868():
    p1, p2, p3, i = map(int, input().split())

    dp = [0] * (i + 1)
    dp[0] = 1

    i1 = i2 = i3 = 0

    for k in range(1, i + 1):
        v1, v2, v3 = dp[i1] * p1, dp[i2] * p2, dp[i3] * p3

        nxt = min(v1, v2, v3)
        dp[k] = nxt

        if nxt == v1: i1 += 1
        if nxt == v2: i2 += 1
        if nxt == v3: i3 += 1

    print(dp[i])

if __name__ == '__main__': boj7868()