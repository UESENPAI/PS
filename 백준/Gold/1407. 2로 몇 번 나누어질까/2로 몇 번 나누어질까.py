from sys import stdin
input = stdin.readline
 
def boj1407():
    A, B = map(int, input().split())

    ans = 0
    k = 0
    while (1 << k) <= B:
        X = (B >> k) - ((A - 1) >> k)
        Y = (B >> (k + 1)) - ((A - 1) >> (k + 1))
        Ck = X - Y
        ans += Ck * (1 << k)
        k += 1

    print(ans)

if __name__ == '__main__': boj1407()