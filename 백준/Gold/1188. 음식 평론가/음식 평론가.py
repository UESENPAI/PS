import sys
input = sys.stdin.readline

def boj1188():
    N, M = map(int, input().strip().split())

    def gcd(N, M):
        if not N % M : return M
        return gcd(M, N % M)

    print(M - gcd(N, M))

if __name__ == '__main__': boj1188()