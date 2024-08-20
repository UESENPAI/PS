from sys import stdin, stdout
input = stdin.readline

def boj15717():
    N = int(input())
    if not N:
        print(1)
        return
    
    MOD = 1000000007

    result = 1
    a, b = 2, N-1

    while b > 0:
        if b&1:
            result*=a
            result%=MOD
        a *= a
        a %= MOD
        b >>= 1

    print(result)     

if __name__ == "__main__": boj15717()