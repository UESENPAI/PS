import sys

N = int(sys.stdin.readline())
if N<1 or N>100: raise Exception(f'Wrong Input')

num=list(map(int, sys.stdin.readline().split()))

v = int(sys.stdin.readline())
if v<-100 or v>100: raise Exception(f'Wrong Input')

v = num.count(v)

print(f'{v}')
