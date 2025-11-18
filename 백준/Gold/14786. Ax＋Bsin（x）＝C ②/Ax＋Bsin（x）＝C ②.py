from sys import stdin
input = stdin.readline
 
def boj14786():
    A, B, C = map(int, input().split())
    import math

    x = C / A

    for _ in range(100):
        fx = A * x + B * math.sin(x) - C
        dfx = A + B * math.cos(x)

        if abs(fx) < 1e-15: break

        if abs(dfx) < 1e-8:
            lam = abs(dfx) / 1e-8 
            if lam < 1e-4: lam = 1e-4
            dx = -(fx / dfx) * lam
        else:
            dx = -(fx / dfx)

        x_new = x + dx

        if x_new < 0: x_new = 0.0

        x = x_new

    print("{:.15f}".format(x))

if __name__ == '__main__': boj14786()