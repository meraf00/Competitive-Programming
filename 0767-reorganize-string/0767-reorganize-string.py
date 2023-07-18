class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        
        heap = []
        
        for char, freq in counter.items():
            heap.append((-freq, char))
                
        heapify(heap)
        
        reordered = [""]                      
        
        while heap:
            # most commoon char         
            freq_1, char_1= heappop(heap)
                        
            
            if char_1 == reordered[-1] and heap:
                freq_2, char_2 = heappop(heap)
                
                reordered.append(char_2)
                
                if freq_2 + 1 < 0:
                    heappush(heap, (freq_2 + 1, char_2) )
                
                heappush(heap, (freq_1, char_1))
                
                continue
            
            elif char_1 == reordered[-1]:
                break
                
            else:
                reordered.append(char_1)
                
                if freq_1 + 1 < 0:
                    heappush(heap, (freq_1 + 1, char_1))
                    
                
            
        reordered = "".join(reordered)
        if len(reordered) != len(s):
            return ""
        
        return reordered
            
        
        