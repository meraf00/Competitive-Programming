class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = Counter(s)
        
        heap = []
        
        for char, freq in counter.items():
            heap.append((ord('a') - ord(char), -freq))                        
        heapify(heap)
        
        
        reordered = [""]
        repeat = repeatLimit
        
        while heap:            
            char_1, freq_1 = heappop(heap)
            
            
            if char_1 == reordered[-1]:
                repeat -= 1
            
            else:
                repeat = repeatLimit                        
            
            # repeat limit reached thus we can't use most common char
            if repeat <= 0:                                                 
                if not heap:
                    break                    
                        
                char_2, freq_2 = heappop(heap)                                
                
                reordered.append(char_2)
                
                if freq_2 + 1 < 0:
                    heappush(heap, (char_2, freq_2 + 1))
                
                heappush(heap, (char_1, freq_1))
            
            else:
                reordered.append(char_1)                
                if freq_1 + 1 < 0:
                    heappush(heap, (char_1, freq_1 + 1))
                
        return "".join(map(lambda x: chr(-x + ord('a')), reordered[1:]))
        