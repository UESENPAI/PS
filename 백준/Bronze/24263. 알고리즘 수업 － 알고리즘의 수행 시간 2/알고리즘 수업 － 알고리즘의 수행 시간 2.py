import sys

n = int(sys.stdin.readline().strip())

def MenOfPassion(A, n):
    vsum = 0
    for i in range(1, n+1):
        i = [n//2];
        vsum+=A[i]
    return vsum

print(f'{n}\n1')