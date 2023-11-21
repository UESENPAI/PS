import sys

N, M = map(int, sys.stdin.readline().strip().split())

basket = [bsk for bsk in range(N+1)]

def dohyun(i, j, k):
    global basket
    tmp = basket[k:j+1] + basket[i:k]
    for idx, e in enumerate(tmp):
        basket[i+idx]=e

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    dohyun(i, j, k)

basket.pop(0)
print(*basket)
