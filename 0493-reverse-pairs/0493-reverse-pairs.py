class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        counter = 0
        
        def merge_sort(arr, left, right):
            if left == right:
                return [arr[left]]
            
            mid = (left + right) // 2
            
            left_arr  = merge_sort(arr, left, mid)            
            
            right_arr = merge_sort(arr, mid + 1, right)            
            
            return merge(left_arr, right_arr)
        
        def merge(arr_1, arr_2):
            nonlocal counter
            
            p1 = 0
            p2 = 0

            l1 = len(arr_1)
            l2 = len(arr_2)

            merged = []
            
            pointer = 0
            while p1 < l1 and p2 < l2:        
                if arr_1[p1] < arr_2[p2]:                                             
                    merged.append(arr_1[p1])
                    p1 += 1                                        

                else:     
                    
                    while pointer < len(arr_1) and arr_1[pointer] <= 2 * arr_2[p2]:
                        pointer += 1
                                        
                    counter += len(arr_1) - pointer
                    
                    merged.append(arr_2[p2])
                    p2 += 1


            merged.extend(arr_1[p1:])
            
            
            for num in arr_2[p2:]:
                while pointer < len(arr_1) and arr_1[pointer] <= 2 * arr_2[p2]:
                        pointer += 1
                                        
                counter += len(arr_1) - pointer

                merged.append(arr_2[p2])
                p2 += 1

            return merged
    
        merge_sort(nums, 0, len(nums) - 1)
        
        return counter
            