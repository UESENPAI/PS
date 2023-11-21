import sys

n = int(sys.stdin.readline().strip())

def MenOfPassion(A, n):
    rsum = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            for k in range(j+1, n+1):
                rsum+=A[i]*A[j]*A[k]
    return rsum

print(f'{((n-1)*(n-2)*(2*n-3)+3*(n-1)*(n-2))//12}\n3')
