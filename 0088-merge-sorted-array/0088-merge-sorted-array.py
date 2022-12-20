class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """ 
        #  shift the numbers
        for i in range(len(nums1)-1,n-1,-1):            
            nums1[i] = nums1[i-n]
        
        
        # merge
        k = 0
        
        i = n
        j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:                
                nums1[k] = nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        
        while j < len(nums2):
            nums1[k] = nums2[j]
            j += 1
            k += 1
                

