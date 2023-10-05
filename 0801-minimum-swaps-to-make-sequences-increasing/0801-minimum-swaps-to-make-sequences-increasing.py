class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        unswapped = [float('inf')] * n
        unswapped[0] = 0
        
        swapped = [float('inf')] * n
        swapped[0] = 1
        
        for i in range(1, n):
            # prev not swapped
            # 2 cases
            # curr unswapped valid
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                unswapped[i] = min(unswapped[i], unswapped[i - 1])
            
            # curr swapped valid
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                # swap prev or curr                
                swapped[i] = min(swapped[i], unswapped[i - 1] + 1)
            
            # prev swapped valid
            # 2 cases
            # curr unswapped valid
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                unswapped[i] = min(unswapped[i], swapped[i - 1])
            
            # curr swapped valid
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                # swap prev or curr                
                swapped[i] = min(swapped[i], swapped[i - 1] + 1)            
          
        
        return min(swapped[-1], unswapped[-1])
            
            