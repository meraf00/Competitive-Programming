class Solution:
    def swap(self, nums, index_1, index_2):
        nums[index_1], nums[index_2] = nums[index_2], nums[index_1]
        
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        positives = []
        negatives = []
        
        for num in nums:                                    
            if num > 0:                
                positives.append(num)
            
            else:
                negatives.append(num)
        
        index = 0
        for positive_num, negative_num in zip(positives, negatives):
            nums[index] = positive_num
            nums[index + 1] = negative_num
            index += 2
        
        return nums
            