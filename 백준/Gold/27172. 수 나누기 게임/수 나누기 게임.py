import sys
input = sys.stdin.readline

def boj27172():
    N = int(input().strip())
    xn = list(map(int,input().strip().split()))

    def getScores():
        nonlocal N, xn
        setxn = set(xn)
        xmax = max(xn)
        sieve = [0] * (xmax+1)
        for x in xn:
            if x == xmax: continue
            for n in range(x<<1, xmax+1, x):
                if n in setxn:
                    sieve[x]+=1
                    sieve[n]-=1
        for x in xn: print(sieve[x], end=' ')

    getScores()
                 
if __name__ == '__main__': boj27172()