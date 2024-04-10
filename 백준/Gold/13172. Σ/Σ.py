import sys
from math import gcd
input = sys.stdin.readline

def boj13172():
    M = int(input().strip())
    NS = [list(map(int, input().strip().split())) for _ in range(M)]
    X = 1000000007

    def getNsquare(num, exp):
        nonlocal X
        result, base = 1, num
        
        while exp > 0:
            if exp % 2:
                result = (result * base) % X
                exp -= 1
            else:
                base = (base * base) % X
                exp >>= 1        
        return result
    
    ans = 0
    for n, s in NS:
        div = gcd(n,s)
        if div != 1:
            n //= div
            s //= div
        getNsquare = lambda S: pow(n, X - 2, X)
        ans += (s*(getNsquare(n))) % X
        #ans += (s*(getNsquare(n,X-2))) % X
    print(ans%X)

if __name__ == '__main__': boj13172()
