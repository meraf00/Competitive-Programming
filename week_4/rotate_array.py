"""
https://leetcode.com/problems/rotate-array/
"""

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """                        
        
        k %= len(nums)
        
        if k == 0:
            return 
        
        temp = nums[len(nums)-k:]
        
        for i in range(len(nums)-1, k-1, -1):            
            nums[i] = nums[i - k]
        
        for i, n in enumerate(temp):
            nums[i] = n


"""
Other Implementation that failed
	
Input: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
38
Output: [17,18,19,20,21,22,24,25,26,27,23,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
Expected: [17,18,19,20,21,22,23,24,25,26,27,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:  
        k = k % len(nums)
        
        if k == 0:
            return                 
        
        bp = 0  # backup pointer
        cp = k  # current item pointer
                        
        while cp < len(nums):
            for bp in range(k):                
                nums[cp % len(nums)], nums[bp] = nums[bp] , nums[cp % len(nums)]
                cp += 1               
"""