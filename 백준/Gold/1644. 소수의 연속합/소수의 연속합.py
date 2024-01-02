import sys
input = sys.stdin.readline

def boj1644():
    N = int(input().strip())

    def era_seive(N):
        sieve = [True] * (N+1)
        for i in range(2, N+1):
            if sieve[i]:
                for j in range(2*i, N+1, i): sieve[j] = False

        return [i for i in range(2, N+1) if sieve[i]]

    primes = era_seive(N)
    ans, fptr, bptr = 0, 0, 0
    while not bptr > len(primes):
        subsum = sum(primes[fptr:bptr])
        if subsum == N:
            ans += 1
            bptr += 1
        elif subsum < N: bptr+=1
        else: fptr+=1
    print(ans)

if __name__ == '__main__': boj1644()