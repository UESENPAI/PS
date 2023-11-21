import sys

K, N = map(int,sys.stdin.readline().strip().split())

L = [int(sys.stdin.readline().strip()) for _ in range(K)]

alpha, omega = 1, max(L)

while alpha <= omega:
    mid = (alpha + omega) // 2
    lines = 0
    for l in L: lines += l // mid #분할 된 랜선 수
    if lines >= N: alpha = mid + 1
    else: omega = mid - 1
print(omega)