import sys

N = int(sys.stdin.readline().strip())

tmp=2
while True:
    if N<3 :
        print(N)
        break
    tmp *= 2
    if (tmp >= N):
        print((N - (tmp // 2)) * 2)
        break