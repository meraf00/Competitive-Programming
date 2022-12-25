class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_combined = []
        
        idx_1 = 0
        idx_2 = 0
        
        while idx_1 < len(nums1) and idx_2 < len(nums2):
            if nums1[idx_1] < nums2[idx_2]:
                nums_combined.append(nums1[idx_1])
                idx_1 += 1
            else:
                nums_combined.append(nums2[idx_2])            
                idx_2 += 1
        
        if idx_1 < len(nums1):
            nums_combined.extend(nums1[idx_1:])
        
        if idx_2 < len(nums2):
            nums_combined.extend(nums2[idx_2:])
        
        length = len(nums_combined)
        
        if length % 2 != 0:            
            median = nums_combined[length//2]
        else:
            left = nums_combined[length//2]
            right = nums_combined[(length - 1)//2]
            median = (left + right) / 2
        
        return median