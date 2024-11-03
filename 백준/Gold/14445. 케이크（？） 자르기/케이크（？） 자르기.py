import sys
input = sys.stdin.readline

def boj14445():
    N = int(input().strip())
    print((N + 1)>>1 if N > 1 else 0)

if __name__ == "__main__": boj14445()