from sys import stdin, stdout
input = stdin.readline
print = stdout.write
 
def boj16565():
    from math import comb

    MOD = 10007
    N = int(input().strip())

    x = 0
    for k in range(1, min(13, N>>2) + 1):
        k4 = k<<2
        sig = comb(13, k) * comb(52 - k4, N - k4)
        if k & 1: x += sig
        else: x -= sig
    print(str(x % MOD)+'\n')

if __name__ == '__main__': boj16565()