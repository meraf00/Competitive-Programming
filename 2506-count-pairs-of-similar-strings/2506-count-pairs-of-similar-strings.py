class Solution:
    def generateHash(self, string):
        counter = {c:0 for c in "abcdefghijklmnopqrstuvwxyz"}
        
        for char in string:
            counter[char] += 1
        
        hash_ = 0
        for char in "abcdefghijklmnopqrstuvwxyz":
            hash_ *= 10
            if counter[char] != 0:
                hash_ += 1
            
        return hash_
        
        
    def similarPairs(self, words: List[str]) -> int: 
        
        similar_counter = {}
        
        for hash_ in map(self.generateHash, words):
            if hash_ in similar_counter:
                similar_counter[hash_] += 1
            else:
                similar_counter[hash_] = 1                
        
        output = 0
        for v in similar_counter.values():
            if v > 1:
                output += math.factorial(v) // (2 * math.factorial(v-2))
        return output
        
        
        