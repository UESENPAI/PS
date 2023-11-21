import sys

N, K = map(int,sys.stdin.readline().strip().split())

coin=[]
for n in (range(N)): coin.append(int(sys.stdin.readline().strip()))

cnt = 0
for n in reversed(range(N)):
    cnt += K//coin[n]
    K %= coin[n]

print(cnt)
