import sys
input = sys.stdin.readline
N = int(input().strip())
N %= 5
print("CY") if (N==2 or not N) else print("SK")