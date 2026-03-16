from sys import stdin
input = stdin.readline

def boj15710():
    MOD = 1000000007
    _, _, n = map(int, input().split())
    print(pow(2, 31*(n-1), MOD))

if __name__ == '__main__': boj15710()