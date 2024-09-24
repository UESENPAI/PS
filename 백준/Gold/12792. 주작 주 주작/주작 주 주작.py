import sys
input = sys.stdin.readline

def boj12792():
    N = int(input().strip())
    i = list(map(int, input().strip().split()))

    for x in range(N):
        if i[x] == x + 1:
            print(-1)
            return
    print(1000003)

if __name__ == "__main__": boj12792()