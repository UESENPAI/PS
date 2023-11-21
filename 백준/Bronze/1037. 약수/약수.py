import sys


N = int(sys.stdin.readline().strip())

div = list(map(int,sys.stdin.readline().split()))

print(f'{max(div)*min(div)}')