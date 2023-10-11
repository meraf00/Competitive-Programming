class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        options = []
        
        if a:
            options.append((-a, 'a'))
        
        if b:
            options.append((-b, 'b'))
        
        if c:
            options.append((-c, 'c'))
        
        heapify(options)
        
        string = []
        
        prev = None
        prev_prev = None
        
        while options:            
            count, letter = heappop(options)             
            
            if prev == letter and prev_prev == letter: 
                if options:
                    c, l = heappop(options)                    
                    string.append(l) 
                    c += 1
                    
                    prev_prev = prev
                    prev = l
                    if c:
                        heappush(options, (c, l))
                        
                    heappush(options, (count, letter))
                
                else:
                    break                    
            
            else:
                string.append(letter)
                count += 1
                prev_prev = prev
                prev = letter
                if count:
                    heappush(options, (count, letter))
            
            
        
        return ''.join(string)