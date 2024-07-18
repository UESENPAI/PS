from sys import stdin
from itertools import permutations
input = stdin.readline

def boj13140():
    N = int(input().strip())

    digits = [_ for _ in range(10)]
    for perm in permutations(digits, 7):
        h,e,l,o,w,r,d = perm
        if h and w:
            hello = 10000 * h + 1000 * e + 100 * l + 10 * l + o
            world = 10000 * w + 1000 * o + 100 * r + 10 * l + d
            if hello + world == N:
                print(f"  {hello}")
                print(f"+ {world}")
                print('-'*7)
                print(str(N).rjust(7))
                return
                
    print("No Answer")  

if __name__ == '__main__': boj13140()