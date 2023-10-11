class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapify(nums)
        
        ans = []
        
        while nums:
            ans.append(heappop(nums))
            
        
        return ans