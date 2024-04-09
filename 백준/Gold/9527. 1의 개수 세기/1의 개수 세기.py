import sys
input = sys.stdin.readline

def boj9527():
    A, B = map(int,input().strip().split())

    def fx(x):
        cnt, dgt = 0, 1
        while not dgt > x:
            div = dgt << 1
            cnt += (x // div) * dgt + min(max(x % div - dgt + 1, 0), dgt)
            dgt <<= 1
        return cnt

    sigmafx = lambda A, B: fx(B) - fx(A - 1)
    ans = sigmafx(A, B)
    print(ans)

if __name__ == '__main__': boj9527()