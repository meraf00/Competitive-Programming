class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        num_freq = defaultdict(int)
        
        for num in nums[:k-1]:
            num_freq[num] += 1
        
        left = 0
        
        answer = []
        
        for right in range(k - 1, len(nums)):
            num = nums[right]
            
            num_freq[num] += 1
                        
            
            count = 0
            for n in range(-50, 51):
                count += num_freq[n]
                
                if count >= x:
                    if n < 0:
                        answer.append(n)
                    else:
                        answer.append(0)                        
                    break
                        
            num_freq[nums[left]] -= 1
            
            left += 1
        
        return answer
                