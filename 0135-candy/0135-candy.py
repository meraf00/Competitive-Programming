class Solution:  
    def find_decreasing_ranges(self, ratings):  
        ranges = []
        i = 0
        while i < len(ratings) - 1:
            current = ratings[i]
            next = ratings[i + 1]
            
            if current > next:
                j = i
                for j in range(i + 1, len(ratings)):
                    if j+1>=len(ratings) or ratings[j] <= ratings[j+1]:
                        break
                ranges.append((i, j))
                i = j+1
                continue
            i += 1
                    
        return ranges
    
    def find_increasing_ranges(self, ratings):  
        ranges = []
        i = 0
        while i < len(ratings) - 1:
            current = ratings[i]
            next = ratings[i + 1]
            
            if current < next:
                j = i
                for j in range(i + 1, len(ratings)):
                    if j+1>=len(ratings) or ratings[j] >= ratings[j+1]:
                        break
                ranges.append((i, j))
                i = j+1
                continue
            i += 1
                    
        return ranges
                        
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        
        candies = [1] * len(ratings)  
                
        
        for rang in self.find_increasing_ranges(ratings):            
            length = rang[1] - rang[0] + 1
            for i in range(rang[0], rang[1] + 1):
                candies[i] = max(candies[i], i - rang[0] + 1)
        
        for rang in self.find_decreasing_ranges(ratings):            
            length = rang[1] - rang[0] + 1
            for i in range(rang[0], rang[1] + 1):                                    
                candies[i] = max(candies[i], rang[1] + 1 - i)
                
        
        return sum(candies)
            
