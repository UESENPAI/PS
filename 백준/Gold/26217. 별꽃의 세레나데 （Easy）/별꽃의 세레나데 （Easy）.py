from sys import stdin, stdout
input = stdin.readline

def boj26217():
    N = int(input().strip())
    print(N*sum(1.0 / _ for _ in range(1, N + 1)))

if __name__ == '__main__': boj26217()