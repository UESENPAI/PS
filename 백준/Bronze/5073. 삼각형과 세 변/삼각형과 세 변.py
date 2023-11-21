import sys

while True:
    t1, t2, t3 = map(int,sys.stdin.readline().strip().split())
    stri = {t1, t2, t3}
    if not t1 and not t2 and not t3: break

    if t1+t2+t3 <= 2 * max(stri):
        print('Invalid')
    else:
        if len(stri) == 1:
            print('Equilateral')
        elif len(stri) == 2:
            print('Isosceles')
        else:
            print('Scalene')
