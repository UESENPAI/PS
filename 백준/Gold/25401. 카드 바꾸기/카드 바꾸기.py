import sys
input = sys.stdin.readline

def boj25401():
    N = int(input().strip())
    x = [0]+(list(map(int, input().strip().split())))

    def getnap(x1, d):
        nonlocal N, x
        nap = 0
        for i in range(1, N + 1):
            x1 += d
            if x[i] != x1: nap += 1
        return nap

    ans = sys.maxsize
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            if not ((x[j] - x[i]) % (j - i)):
                d = (x[j] - x[i]) // (j - i)
                ans = min(ans, getnap(x[i] - d * i, d))
    print(ans)

if __name__ == '__main__': boj25401()