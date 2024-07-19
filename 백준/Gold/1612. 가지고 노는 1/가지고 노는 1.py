from sys import stdin
input = stdin.readline

def boj1612():
    N = int(input().strip())

    if N == 1: ans = 1
    elif not N&1 or not N%5: ans = -1
    else:
        x, ans = 1, 1
        while x:
            x += (9*x + 1) % N
            x %= N
            ans += 1
    print(ans)

if __name__ == '__main__': boj1612()