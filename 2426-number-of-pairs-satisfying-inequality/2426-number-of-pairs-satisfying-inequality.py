class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:                      
        nums = [n1 - n2 for n1, n2 in zip(nums1, nums2)]
        
        counter = 0                      
        
        def merge_sort(nums):
            
            length =  len(nums)
            if length <= 1:
                return nums

            left = merge_sort(nums[:length // 2])
            right = merge_sort(nums[length // 2:])

            return merge(left, right)
        
    
        def merge(arr1, arr2):
            nonlocal counter
            
            p1 = 0
            p2 = 0

            l1 = len(arr1)
            l2 = len(arr2)

            merged = []                        
            
            
            while p1 < l1 and p2 < l2:            

                if arr1[p1] <= arr2[p2] + diff:
                    counter += l2 - p2
                    p1 += 1

                else:                                          
                    p2 += 1

            p1 = p2 = 0
            while p1 < l1 and p2 < l2:            

                if arr1[p1] <= arr2[p2]:                    
                    
                    merged.append(arr1[p1])
                    p1 += 1

                else:                      
                    merged.append(arr2[p2])
                    p2 += 1

            
            
            merged.extend(arr1[p1:])
            merged.extend(arr2[p2:])
            
            return merged
        
        
        merge_sort(nums)  
        
        return counter

        