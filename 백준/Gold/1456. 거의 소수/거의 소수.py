import sys
input = sys.stdin.readline

def boj1456():
    A, B = map(int, input().strip().split())

    def eratosthenes(N):
        prime = [False] * (N + 1)
        p = 2
        while p * p <= N:
            if not prime[p]:
                for ptr in range(p * p, N+1, p): prime[ptr] = True
            p += 1
        return [p for p in range(2, N+1) if not prime[p]]

    def getPrimeNSqaure(A, B):
        primes = eratosthenes(int(B**0.5))
        nsprimes = set()
        a, b = A-1, B+1
        for prime in primes:
            pw = 2
            while prime**pw < b:
                if prime**pw > a: nsprimes.add(prime**pw)
                pw += 1
        return len(nsprimes)
    
    ans = getPrimeNSqaure(A, B)
    print(ans)

if __name__ == '__main__': boj1456()