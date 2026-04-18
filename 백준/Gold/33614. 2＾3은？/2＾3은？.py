from sys import stdin
input = stdin.readline

def boj33614():
    T = int(input())
    for _ in range(T):
        p, q, r = map(int, input().split())
        print((p + min(q, r) - 1) % 1000000007)

if __name__ == "__main__": boj33614()