import sys

tri = []

for _ in range(3):
    tri.append(int(sys.stdin.readline().strip()))

stri = set(tri)

if tri[0]+tri[1]+tri[2] != 180:
    print('Error')
else:
    if len(stri) == 1:
        print('Equilateral')
    elif len(stri) == 2:
        print('Isosceles')
    else:
        print('Scalene')
