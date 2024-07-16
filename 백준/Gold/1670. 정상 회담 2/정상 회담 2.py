from sys import stdin
input = stdin.readline

def boj1670():
    N = int(input().strip())
    MOD = 987654321

    def get_catalan(N, MOD):
        C = [0] * (N + 1)
        C[0] = 1
        for i in range(1, N + 1):
            for j in range(i):
                C[i] = (C[i] + C[j] * C[i - 1 - j]) % MOD
        return C[N]

    print(0) if N&1 else print(get_catalan(N>>1, MOD))

if __name__ == '__main__': boj1670()