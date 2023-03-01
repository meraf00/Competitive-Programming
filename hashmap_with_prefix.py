from collections import defaultdict


nums = [2,2,2,1,2,2,2,1,2,2,2]
k = 2

hashmap = defaultdict(int)
odd_counts,res = 0,0
hashmap[0] = 1
for i in range(len(nums)):
    if nums[i]%2 != 0:
        odd_counts+=1
    res += hashmap[odd_counts-k]
    hashmap[odd_counts]+=1

print(res)