import sys
input = sys.stdin.readline

def boj1052():
    N, K = map(int, input().strip().split())

    ans = 0
    while bin(N).count('1') > K:
        lbit = N & -N
        ans += lbit
        N += lbit
    print(ans)
    
if __name__ == '__main__': boj1052()