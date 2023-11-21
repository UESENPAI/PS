import sys

t1, t2, t3 = map(int,sys.stdin.readline().strip().split())

tar = max([t1, t2, t3])

sig = t1+t2+t3

if sig>2*tar:
    print(sig)
else:
    print(2*(sig-tar)-1)
