from sys import stdin
input = stdin.readline
 
def boj14565():
    N, A = map(int, input().split())

    def eea(a, b):
        x0, y0, x1, y1 = 1, 0, 0, 1
        while b:
            q = a // b
            a, b, x0, x1, y0, y1 = b, a - q*b, x1, x0 - q*x1, y1, y0 - q*y1
        return a, x0, y0

    ainv = (N - A) % N
    g, x, y = eea(A, N)
    minv = -1 if g != 1 else x % N
    print(f"{ainv} {minv}")

if __name__ == '__main__': boj14565()