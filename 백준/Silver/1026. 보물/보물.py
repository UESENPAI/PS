import sys
input = sys.stdin.readline

def boj1026():
    N = int(input().strip())
    A = sorted(list(map(int,input().strip().split())),reverse=True)
    B = list(map(int,input().strip().split()))

    def S(X, Y): return sum(a * b for a, b in zip(X, Y))

    print(S(A, sorted(B)))

if __name__ == "__main__": boj1026()