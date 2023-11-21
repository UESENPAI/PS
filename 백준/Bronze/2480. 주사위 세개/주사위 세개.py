import sys

A, B, C = map(int, sys.stdin.readline().split())

s = {A, B, C}

if A<0 or B<0 or C<0 or A>6 or B>6 or C>6: raise Exception('Wrong input range')

if len(s)==1:
    price = 10000 + A*1000
elif len(s)==2:
    if A == B:
        price = 1000 + A*100
    elif B == C:
        price = 1000 + B*100
    else:
        price = 1000 + C*100
else:
    price = max(A, B, C)*100
    
print(f'{price}')
