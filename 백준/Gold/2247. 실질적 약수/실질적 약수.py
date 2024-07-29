from sys import stdin, stdout
input = stdin.readline

def boj2247():
    n = int(input().strip())
    MOD = 1000000
    
    csod = lambda n: sum(i * (n // i - 1) % MOD for i in range(2, (n>>1)+1))

    print(csod(n) % MOD)

if __name__ == '__main__': boj2247()