import sys
input = sys.stdin.readline

def boj2748_formula():
    from math import sqrt
    
    n = int(input().strip())
    r5 = sqrt(5)
    npowof2 = 1 << n 
    print(int(1 / (r5 * npowof2) * ((1 + r5)**n - (1 - r5)**n)))

def boj2748_matrix():
    n = int(input().strip())
    mat = (1, 1, 1, 0)

    def matmul(A,B):
        return (A[0] * B[0] + A[1] * B[2],
            A[0] * B[1] + A[1] * B[3],
            A[2] * B[0] + A[3] * B[2],
            A[2] * B[1] + A[3] * B[3])

    def matpow(A,x):
        res = (1, 0, 0, 1)
        while x > 0:
            if x % 2 == 1: res = matmul(res, A)
            A = matmul(A, A)
            x //= 2
        return res[1]

    print(matpow(mat,n))

if __name__ == "__main__": boj2748_matrix()