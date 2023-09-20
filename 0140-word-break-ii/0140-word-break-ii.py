class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:        
        length = len(s)        
        
        wordDict = set(wordDict)
        
        max_word_length = max(map(len, wordDict))
        
        sentence = []
        sentence_length = 0
        
        ans = set()
        
        def backtrack(idx): 
            nonlocal sentence_length            
            
            if sentence_length == length:
                ans.add(' '.join(sentence))
                return
            
            for i in range(idx, idx + max_word_length + 1):
                word = s[idx : i]
                
                if word in wordDict:
                    word_length = len(word)
                    
                    sentence.append(word)
                    sentence_length += word_length
                    backtrack(i)
                    sentence.pop()
                    sentence_length -= word_length
        
        backtrack(0)
        
        return ans
                
                