from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:        
        map_ = {}
        for i, num in enumerate(nums2):
            map_[num] = i
        
        stack = []
        nextGreatest = [-1] * len(nums2)
        for i in range(len(nums2)):
            if len(stack) == 0 or nums2[stack[-1]] > nums2[i]:
                stack.append(i)
            
            else:
                while len(stack) and nums2[stack[-1]] < nums2[i]:
                    index = stack.pop()
                    nextGreatest[index] = nums2[i]
                stack.append(i)

        nge = []
        for n in nums1:
            index = map_[n]
            nge.append(nextGreatest[index])
        
        return nge