import sys
from math import sqrt

T = int(sys.stdin.readline().strip())

def is_prime(ip):
    end = int(sqrt(ip))+2
    for dv in range(2,end):
        if not ip%dv: return False
    return True

def next_prime(CS):
    if CS<=2: return 2
    while not is_prime(CS):
        CS = CS + 1
    return CS

for _ in range(T):
    CS = int(sys.stdin.readline().strip())
    print(next_prime(CS))
