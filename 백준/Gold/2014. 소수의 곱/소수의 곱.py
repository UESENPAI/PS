import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

def boj2014():
    K, N = map(int, input().strip().split())
    primes = list(map(int, input().strip().split()))

    def getNPrime():
        nonlocal K, N, primes
        heap = [prime for prime in primes]
        heapify(heap)
        
        for _ in range(N):
            minval = heappop(heap)
            for prime in primes:
                ptr = minval * prime
                heappush(heap, ptr)
                if not minval % prime: break
        
        print(minval)

    getNPrime()

if __name__ == '__main__': boj2014()