class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counter = [0] * len(nums)
        
        for i in range(len(nums)):
            nums[i] = (nums[i], i)
            
        def merge_sort(arr, left, right):
            if left == right:
                return [arr[left]]
            
            mid = (left + right) // 2
            
            left_arr  = merge_sort(arr, left, mid)
            right_arr = merge_sort(arr, mid + 1, right)
            
            return merge(left_arr, right_arr)
        
        
        def merge(arr_1, arr_2):            
            p1 = 0
            p2 = 0
            
            l1 = len(arr_1)            
            l2 = len(arr_2)
            
            merged = []
            
            pointer = 0
            
            while p1 < l1 and p2 < l2:
                if arr_1[p1][0] <= arr_2[p2][0]:  
                    while pointer < l2 and arr_2[pointer][0] < arr_1[p1][0]:
                        pointer += 1
                    
                    counter[arr_1[p1][1]] += pointer
                    
                    merged.append(arr_1[p1])
                    p1 += 1
                
                else:                                          
                    merged.append(arr_2[p2])
                    p2 += 1
                
                
            merged.extend(arr_2[p2:])
            
            for num, idx in arr_1[p1:]:
                
                while pointer < l2 and arr_2[pointer][0] < num:                    
                    pointer += 1
                
                counter[idx] += pointer
                
                merged.append((num, idx))                


            return merged
        
        
        merge_sort(nums, 0, len(nums) - 1)
        
        return counter
                    