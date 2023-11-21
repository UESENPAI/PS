import sys

N, M = map(int,sys.stdin.readline().split())

off = set()
for n in range(N):
    off.add(sys.stdin.readline().strip())

brand = []
for m in range(M):
    brand.append(sys.stdin.readline().strip())

off_brand = list(set.intersection(off, brand))
off_brand.sort()

print(len(off_brand))
for ob in off_brand:
    print(ob)