import sys

n = int(sys.stdin.readline().strip())

def MenOfPassion(A, n):
    rsum = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            rsum+=A[i]*A[j]
    return rsum

print(f'{sum(range(1,n))}\n2')