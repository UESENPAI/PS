from sys import stdin, stdout
from math import lcm
input = stdin.readline
 
def boj1490():
    N = int(input().strip())
    a = [int(n) for n in str(N)]

    def lcms(a):
        c = a[0]
        for b in a[1:]:
            if b: c = lcm(c, b)
        return c

    l=lcms(a)
    #print(l)

    if N % l:
        cnt = 1
        while True:
            for i in range(0, 10**cnt):
                c = int(str(N) + "0"*(cnt-len(str(i))) + str(i))
                #print(c)
                if not c % l:
                    print(c)
                    return
            cnt += 1
    else:
        print(N)

if __name__ == '__main__': boj1490()