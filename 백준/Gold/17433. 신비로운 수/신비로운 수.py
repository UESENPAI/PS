from sys import stdin, stdout
input = stdin.readline
 
def boj17433():
    from math import gcd
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        arr = list(map(int, input().split()))
        g = 0
        for i in range(1, N): g = gcd(g, abs(arr[i] - arr[0]))
        print(g) if g else print("INFINITY")

if __name__ == '__main__': boj17433()