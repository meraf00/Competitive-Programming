class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        nums.sort()
        
        target = len(nums) - 1         
        
        freq = Counter(nums)
        
        min_ops = float('inf')
        
        unique = sorted(freq.keys())
        duplicate_count = [0]
        
        for num in unique:
            duplicate_count.append(duplicate_count[-1] + freq[num] - 1)                    
                
        for i in range(n):
            right = bisect_right(nums, nums[i] + target)
                    
            window_size = right - i
            
            left_out = n - window_size
                                    
            duplicates = 0
            
            a = bisect_left(unique, nums[i])
            b = bisect_right(unique, nums[i] + target)
                        
            duplicates = duplicate_count[b] - duplicate_count[a]
            
            min_ops = min(min_ops, duplicates + left_out)                        
        
        return min_ops
        