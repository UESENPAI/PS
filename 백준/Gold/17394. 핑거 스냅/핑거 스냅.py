from sys import stdin, stdout
from collections import deque
input = stdin.readline

def boj17394():
    T = int(input().strip())
    NAB = [tuple(map(int, input().strip().split())) for _ in range(T)]

    is_prime = [False, False] + [True] * 99999

    for i in range(2, 100001):
        if is_prime[i]:
            for j in range(i<<1, 100001, i): is_prime[j] = False
    

    def bfs(N, A, B):
        nonlocal is_prime
        
        primes = set()
        for p in range(A, B+1):
            if is_prime[p]: primes.add(p)

        if not primes:
            print(-1)
            return
        
        q = deque([N])
        dp = {N: 0}
        ans = -1
        
        while q:
            n = q.popleft()
            if n in primes:
                ans = dp[n]
                break

            for next in filter(lambda x: not (x in dp or x<0), [n>>1, n//3, n+1, n-1]):
                dp[next] = dp[n] + 1
                q.append(next)

        print(ans)
    

    for N,A,B in NAB: bfs(N, A, B)

if __name__ == '__main__': boj17394()