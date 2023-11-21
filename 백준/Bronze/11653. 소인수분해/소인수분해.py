import sys

N = int(sys.stdin.readline())
if N<1 or N>10000000: raise Exception(f'input error')

while N > 1:
    ftr = 2
    while N % ftr !=0:
        ftr = ftr + 1
    N=N//ftr
    print(f'{ftr}')
