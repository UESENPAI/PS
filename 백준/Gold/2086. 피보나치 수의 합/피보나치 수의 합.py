import sys
input = sys.stdin.readline

def boj2086():
    a, b = map(int, input().strip().split())
    MOD = 1000000000

    def matmul(A, B):
        nonlocal MOD
        return [[(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
                [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]]

    def matpow(M, power):
        nonlocal MOD
        result = [[1, 0], [0, 1]]
        base = M
        while power:
            if power % 2: result = matmul(result, base)
            base = matmul(base, base)
            power>>=1
        return result

    def getfibo(n):
        nonlocal MOD
        if not n: return 0
        elif n == 1: return 1
        else:
            F = [[1, 1], [1, 0]]
            result = matpow(F, n - 1)
            return result[0][0]

    getfibosum = lambda n: (getfibo(n + 2) - 1) % MOD

    ans = getfibosum(b) - getfibosum(a-1)
    ans %= MOD
    
    print(ans)

if __name__ == '__main__': boj2086()