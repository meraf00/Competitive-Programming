from typing import List

class Solution:
    
    def insertionSort1(self, n: int, arr: List[int]) -> None:        
        unsorted_element = arr[-1]
    
        for i in range(n-2, -2, -1):      
            if arr[i] > unsorted_element:            
                arr[i + 1] = arr[i]
                
                if i == -1:
                    arr[0] = unsorted_element
                                            
                print (" ".join(map(str, arr)))
                
            else:
                arr[i + 1] = unsorted_element
                print (" ".join(map(str, arr)))

                break


