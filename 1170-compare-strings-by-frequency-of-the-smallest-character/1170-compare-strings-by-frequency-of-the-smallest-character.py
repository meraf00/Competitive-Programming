class Solution:
    def frequency(self, word):
        smallest_char = min(word)
        
        return Counter(word)[smallest_char]                
    
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        queries = list(map(self.frequency, queries))
        
        words = list(map(self.frequency, words))
        
        words.sort()
        
        length = len(words)
        
        for index, query in enumerate(queries):
            insertion_index = bisect_right(words, query)
            
            # print(insertion_index, "<<", query, words)
            
            # if words[insertion_index] ==  query:
                
            queries[index] = length - insertion_index
        
        return queries
