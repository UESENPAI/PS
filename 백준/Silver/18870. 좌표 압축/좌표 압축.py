import sys
from collections import Counter

N = int(sys.stdin.readline())
if N<1 or N>1000000: raise Exception('Wrong Input!')

X = list(map(int,sys.stdin.readline().split()))
if len(X) != N: raise Exception('Wrong Input!')

XS = sorted(list(set(X)))
dic = {XS[i] : i for i in range(len(XS))}

for x in X:
    if x<-10**9 or x>10**9: raise Exception('Wrong Input!')
    print(dic[x], end = ' ')
