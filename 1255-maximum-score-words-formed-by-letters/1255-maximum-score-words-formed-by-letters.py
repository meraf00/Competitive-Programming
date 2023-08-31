class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n_words = len(words)
        letter_count = Counter(letters)                          
        
        def get_word_score(word, letter_count):
            word_letters = Counter(word)                        
            
            word_score = 0
            
            for char in word:
                if word_letters[char] > letter_count.get(char, 0):                   
                    return 0
                
                word_score += score[ord(char) - 97]
            
            return word_score
        
        max_score = 0
        current_score = 0
                
        def backtrack(word_idx):
            nonlocal max_score, current_score                        
            
            if word_idx >= n_words:
                max_score = max(max_score, current_score)
                return                        
            
            word_score = get_word_score(words[word_idx], letter_count)

            if word_score > 0:
                current_score += word_score
                for char in words[word_idx]:
                    letter_count[char] -= 1

                backtrack(word_idx + 1)

                for char in words[word_idx]:
                    letter_count[char] += 1
                current_score -= word_score

            backtrack(word_idx + 1)
                                
        
        backtrack(0)
        
        return max_score