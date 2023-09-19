class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:        
        nums.sort(reverse=True)
        
        non_included_elements_sum = sum(nums)
        
        seq = []
        seq_sum = 0
        
        for num in nums:
            seq.append(num)
            
            seq_sum += num
            non_included_elements_sum -= num
                                                
            if seq_sum > non_included_elements_sum:
                break
        
        return seq
            