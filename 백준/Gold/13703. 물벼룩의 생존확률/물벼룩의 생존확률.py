from sys import stdin, stdout
input = stdin.readline
 
def boj13703():
    k, n = map(int, input().split())

    dp = [[-1]*128 for _ in range(128)]

    def swim(sec: int, loc: int):
        if dp[sec][loc] != -1: return dp[sec][loc]
        if not loc:
            dp[sec][loc] = 2 << (sec - 1) if sec else 1
            return 2 << (sec - 1) if sec else 1
        if not sec: return 0

        dp[sec][loc] = swim(sec-1, loc-1) + swim(sec-1, loc+1)
        return dp[sec][loc]

    swim(n, k)
    print((2<<(n-1)) - dp[n][k])

if __name__ == '__main__': boj13703()