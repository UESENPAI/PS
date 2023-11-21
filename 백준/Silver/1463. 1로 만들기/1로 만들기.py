import sys

X = int(sys.stdin.readline().strip())

dp = {1:0}

def rec(n):
    if n in dp.keys():
        return dp[n]
    if not n%6:
        dp[n]=min(rec(n//3)+1, rec(n//2)+1)
    elif not n%3:
        dp[n]=min(rec(n//3)+1, rec(n-1)+1)
    elif not n%2:
        dp[n]=min(rec(n//2)+1, rec(n-1)+1)
    else:
        dp[n]=rec(n-1)+1
    return dp[n]

print(rec(X))          
