import sys
from functools import reduce
input = sys.stdin.readline

def boj1924():
    x, y = (map(int,input().strip().split()))

    days = {key: value % 7 for key, value in {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }.items()}

    ans = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

    print(ans[(y + sum(days[m] for m in range(x - 1, 0, -1))) % 7])

if __name__ == "__main__": boj1924()