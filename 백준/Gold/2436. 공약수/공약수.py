import sys
from math import sqrt, gcd
input = sys.stdin.readline

def boj2436():
    GCD, LCM = map(int,input().strip().split())

    remnants = LCM // GCD

    def getFactors(d):
        factors = []
        for div in range(1, int(sqrt(d)) + 1):
            if d % div == 0: factors.append((div, d // div))
        return factors

    factors = getFactors(remnants)
    
    ans = sys.maxsize
    for a, b in factors:
        if gcd(a, b) == 1:
            sbuffer = a * GCD + b * GCD
            if sbuffer < ans:
                ans = sbuffer
                result = (a * GCD, b * GCD)
                
    print(f"{min(result)} {max(result)}")    

if __name__ == '__main__': boj2436()