from sys import stdin
input = stdin.readline

def boj13258():
    N = int(input())
    arr = list(map(int, input().split()))
    J = int(input())
    C = int(input())

    S0 = sum(arr)
    x0 = arr[0]

    result = x0 * (S0 + C * J) / S0

    print(result)

if __name__ == '__main__': boj13258()