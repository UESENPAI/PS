import sys
input = sys.stdin.readline

def boj24511():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    M = int(input().strip())
    C = list(map(int, input().strip().split()))

    B = [B[i] for i, a in enumerate(A) if not a][::-1]+C
    print(*B[:M])

if __name__ == "__main__":
    boj24511()