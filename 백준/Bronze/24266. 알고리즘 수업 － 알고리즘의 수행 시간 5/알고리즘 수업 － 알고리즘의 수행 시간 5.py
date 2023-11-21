import sys

n = int(sys.stdin.readline().strip())

def MenOfPassion(A, n):
    rsum = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                rsum+=A[i]*A[j]*A[k]
    return rsum

print(f'{n**3}\n3')
