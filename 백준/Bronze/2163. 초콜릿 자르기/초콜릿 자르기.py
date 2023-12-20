import sys

input = sys.stdin.readline

def boj2163():
    N, M = map(int,input().strip().split())
    print(N*M-1)

if __name__ == "__main__": boj2163()