import sys
from collections import Counter

T = int(sys.stdin.readline())
if T<1 or T>1000: raise Exception('Wrong Input!')

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

def recursion(s, l, r):
    global cnt
    cnt = cnt + 1
    if(l>=r): return 1
    elif s[l]!=s[r]: return 0
    else: return recursion(s, l+1, r-1)

s = []
for i in range(T):
    s.append(sys.stdin.readline().rstrip())
    if len(s[i])<1 or len(s[i])>1000: raise Exception('Wrong Input!')
    cnt = 0
    print(isPalindrome(s[i]),cnt)