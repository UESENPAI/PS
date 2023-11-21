import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    s = sys.stdin.readline().strip()
    print(f'{s[0]}{s[-1]}')