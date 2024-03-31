import sys
from math import factorial
input = sys.stdin.readline

def boj1722():
    N = int(input().strip())
    k = list(map(int,input().strip().split()))
    qnum = k.pop(0)

    def getkseq(k):
        nonlocal N, nums, ans
        while len(ans) < N:
            if len(ans) == N-1:
                ans.append(nums[-1])
                break
            cases = factorial(len(nums)-1)
            seq = (k - 1) // cases
            ans.append(nums.pop(seq))
            k -= seq * cases
            
        print(*ans)

    def getkord(k):
        nonlocal N, nums, ans    
        for num in k:
            cases = factorial(N) // N
            idx = nums.index(num)
            if len(nums) == 2:
                idx += 1
                ans.append(cases*idx)
                print(sum(ans))
                return
            nums.pop(idx)
            ans.append(cases*idx)
            N -= 1  
            
    nums = list(range(1, N+1))
    ans = []
    if qnum == 1: getkseq(k.pop())
    elif qnum == 2: getkord(k)
    

if __name__ == '__main__': boj1722()