import sys

a, b, c, d, e, f = map(int,sys.stdin.readline().strip().split())

assert a*e-b*d
x = int((e*c-b*f)//(a*e-b*d))
y = int((-d*c+a*f)//(a*e-b*d))

print(f'{x} {y}')
