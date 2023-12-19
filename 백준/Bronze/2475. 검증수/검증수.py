import sys
from functools import reduce
input = sys.stdin.readline

def boj2475():
    arr = list(map(int,input().strip().split()))
    result = reduce(lambda x, y: x + y, map(lambda x: x**2, arr)) % 10
    print(result)

if __name__ == "__main__": boj2475()