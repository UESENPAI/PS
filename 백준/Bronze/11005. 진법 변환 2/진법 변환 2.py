import sys

N,B = map(int, sys.stdin.readline().strip().split())

nums="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans=str()

while N:
    ans+=nums[N%B]
    N//=B

print(ans[::-1])
