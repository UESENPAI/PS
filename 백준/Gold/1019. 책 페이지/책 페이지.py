import sys
input = sys.stdin.readline

def boj1019():
    N = input().strip()
    d = {i: 0 for i in range(10)} 

    k = len(N)
    for x in N:
        k-=1
        for i in range(int(x)):
            d[i]+=10**k
            for j in range(10):
                if k>=1:
                    d[j]+=(10**(k-1))*k
        d[0]-=10**k
        if k: d[int(x)]+=(int(''.join(N[-k:]))+1)
        else: d[int(x)]+=1

    for i in range(10): print(d[i], end=' ')

if __name__ == '__main__': boj1019()
