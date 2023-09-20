class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        
        map_for_max = ''
        map_for_min = num[0]
        
        for i in num:
            if i != '9':
                map_for_max = i
                break
        
        
        max_val = []
        min_val = []
        
        for digit in num:
            if digit == map_for_max:
                max_val.append('9')
            
            else:
                max_val.append(digit)
            
            if digit == map_for_min:
                min_val.append('0')
            
            else:            
                min_val.append(digit)
        
        max_val = int(''.join(max_val))
        min_val = int(''.join(min_val))
        
        return max_val - min_val