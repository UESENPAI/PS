import sys

n = int(sys.stdin.readline())

code1, code2 = 0, 0

def fib(n):
    global code1
    if n==1 or n==2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))

dp = [None for _ in range(n+1)]
dp[1] = dp[2] = 1
def fibonacci(n):
    global code2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        code2 += 1
    return code2
    

code1 = fib(n)
code2 = n-2
print(f'{code1} {code2}')
