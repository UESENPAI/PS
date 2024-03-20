import sys
input = sys.stdin.readline

def boj11689():
    N = int(input().strip())
    
    def eulerphi(N):
        result = N
        p = 2 

        while p * p <= N:
            if N % p == 0:
                while N % p == 0: N //= p
                result -= result // p
            p += 1

        if N > 1: result -= result // N

        return result

    print(eulerphi(N))

if __name__ == '__main__': boj11689()