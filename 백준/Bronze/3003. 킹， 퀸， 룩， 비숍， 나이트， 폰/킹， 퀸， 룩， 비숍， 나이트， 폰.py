import sys

data = list(map(int, sys.stdin.readline().split()))

answer = [1, 1, 2, 2, 2, 8]

for dat, ans in zip(data, answer):
    print(ans - dat)