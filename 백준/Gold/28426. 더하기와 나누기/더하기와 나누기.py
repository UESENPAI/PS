import sys
input = sys.stdin.readline

def boj14671():
    N = int(input().strip())

    if N == 1:
        print(2)
        return

    evens = [2 * i for i in range(1, N)]
    mod = (N * (N - 1)) % 3

    if mod == 1:
        evens[-1] += 2
    elif mod == 2:
        evens[-1] += 4

    ans = [3] + evens
    print(" ".join(map(str, ans)))

if __name__ == "__main__": boj14671()