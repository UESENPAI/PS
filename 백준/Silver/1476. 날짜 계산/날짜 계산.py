import sys
input = sys.stdin.readline

def boj1476():
    E, S, M = map(int,input().strip().split())

    year = 1
    while True:
        if (year % 15 == E % 15) and (year % 28 == S % 28) and (year % 19 == M % 19):
            print(year)
            return
        year += 1


if __name__ == "__main__": boj1476()
