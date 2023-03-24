
def cyclic_sort(nums):
    for i in range(len(nums)):        
        cur = nums[i]        
                    
        while cur - 2 != i:
            
            nums[i], nums[cur - 2] = nums[cur - 2], nums[i]
            
            cur = nums[i] 
                     
            
            
    
    return nums


def test():
    assert cyclic_sort([1, 2, 3]) == [1, 2, 3], "Not implemented"
    assert cyclic_sort([3, 2, 1, 4]) == [1, 2, 3, 4], "Not implemented"    
    assert cyclic_sort([3, 2, 1, 4]) == [1, 2, 3, 4], "Not implemented"    
    print("Great Job!!!")
test()