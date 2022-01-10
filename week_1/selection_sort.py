class Solution: 
    def select(self, arr, i):        
        if arr[i:]:
            return min(arr[i:])
    
    def selectionSort(self, arr,n):        
        for i in range(n):
            selected = self.select(arr, i)
            selected_pos = arr[i:].index(selected) + i
            
            temp = arr[i]
            arr[i] = selected
            
            arr[selected_pos] = temp
