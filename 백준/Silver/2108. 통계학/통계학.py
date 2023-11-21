import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
    
print(round(sum(nums)/n))
    
nums.sort()
print(nums[n // 2])

nums_s = Counter(nums).most_common()
if len(nums_s) > 1:
    if nums_s[0][1] == nums_s[1][1]:
        print(nums_s[1][0])
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])
    
print(nums[-1] - nums[0])