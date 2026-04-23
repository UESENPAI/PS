from sys import stdin
input = stdin.readline

def boj14488():
    N, T_str = input().split()
    N = int(N)

    if '.' in T_str:
        a, b = T_str.split('.')
        b = (b + '0000')[:4]
    else:
        a = T_str
        b = '0000'
    T = int(a) * 10000 + int(b)

    X = list(map(int, input().split()))
    V = list(map(int, input().split()))

    L = -10**30
    R = 10**30

    for i in range(N):
        lft = X[i] * 10000 - T * V[i]
        rgt = X[i] * 10000 + T * V[i]

        if lft > L:
            L = lft
        if rgt < R:
            R = rgt

    print(1 if L <= R else 0)

if __name__ == "__main__": boj14488()