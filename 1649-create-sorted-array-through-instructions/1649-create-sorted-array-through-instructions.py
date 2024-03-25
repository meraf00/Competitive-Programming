class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:                        
        def merge(arr1, arr2):
            arr1.append((float('inf'), 0, 0))
            arr2.append((float('inf'), 0, 0))
            
            
            p1 = 0
            p2 = 0
            
            result = []
                        
            less_ptr = 0
            great_ptr = 0
            
            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1][0] <= arr2[p2][0]:
                    result.append(arr1[p1])
                    p1 += 1
                
                else:
                    while less_ptr < len(arr1) and arr1[less_ptr][0] < arr2[p2][0]:
                        less_ptr += 1
                    
                    while great_ptr < len(arr1) and arr1[great_ptr][0] <= arr2[p2][0]:
                        great_ptr += 1
                    
                    result.append((arr2[p2][0], 
                                   arr2[p2][1] + less_ptr, 
                                   arr2[p2][2] + len(arr1) - great_ptr - 1))
                    p2 += 1
            
            result.pop()
            
            return result
                    
            
        def merge_sort(left, right, arr):
            if right == left:
                return [arr[right]]
            
            mid = (right + left) // 2
            left_arr = merge_sort(left, mid, arr)
            right_arr = merge_sort(mid + 1, right, arr)
            
            return merge(left_arr, right_arr)
        
        
        for i, ins in enumerate(instructions):
            instructions[i] = (ins, 0, 0)
            
        ans = merge_sort(0, len(instructions) - 1, instructions)
        
        
        
        total = 0
        for num, less, greater in ans:
            total += min(less, greater)
            
        mod = pow(10, 9) + 7
        return total % mod
        