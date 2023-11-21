import sys

N, k = map(int, sys.stdin.readline().split())
if N<1 or N>1000 or k<1 or k>N: raise Exception('Wrong Input!')

score = list(map(int,sys.stdin.readline().split()))
if len(score) != N: raise Exception('Wrong Input!')

score.sort()
                                    
for s in score:
    if s<0 or s>10000: raise Exception('Wrong Input!')

print(f'{score[-k]}')
