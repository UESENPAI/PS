import sys

S = sys.stdin.readline().strip()

def ispalindrome(S):
    for s in range(len(S)//2):
        if S[s] != S[-s-1]:
            return False
    return True

if ispalindrome(S): print(1)
else: print(0)
