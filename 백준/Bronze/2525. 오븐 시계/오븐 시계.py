import sys

A, B = map(int, sys.stdin.readline().split())

if A<0 or A>23 or B<0 or B>59: raise Exception('입력 범위가 잘못되었습니다')

C=int(sys.stdin.readline())

if C<0 or C>1000: raise Exception('입력 범위가 잘못되었습니다')

B = B + C

if B>=60:
    C = B//60
    B = B - C*60
    A = A+C
    if A>=24:
        A=A-24

print(f'{A} {B}')
