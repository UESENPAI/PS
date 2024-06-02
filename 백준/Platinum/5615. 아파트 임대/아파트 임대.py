import sys
from math import sqrt
input = sys.stdin.readline

def Miller_Rabin(N, a):

    def powmod(a, b, N):
        if b<2: return pow(a,b)%N
        else: return a*pow(powmod(a,b>>1,N),2)%N if b%2 else pow(powmod(a, b>>1, N),2)%N
            
    r, d = 0, N - 1
    while not d % 2:
        r += 1
        d >>= 1
    x = powmod(a, d, N)
    if x == 1 or x+1 == N: return True
    for _ in range(r-1):
        x = powmod(x, 2, N)
        if x+1 == N: return True
    return False

def isprime(a):
    primes = [2,13,23,1662803]
    if a in primes : return True
    if a==1 or not a%2: return False
    for p in primes:
        if not Miller_Rabin(a, p): return False
    return True

def boj5615():
    N = int(input().strip())
    A = [int(input().strip()) for _ in range(N)]
    
    ans = 0
    for a in A:
        if isprime(1+(a<<1)): ans+=1
    print(ans)

if __name__ == '__main__': boj5615()