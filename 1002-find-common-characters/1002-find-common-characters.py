class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        global_counter = [0] * 26
        
        for index, word in enumerate(words):            
            counter = [0] * 26
            for char in word:
                char_index = ord(char) - 97
                counter[char_index] += 1
            
            # take the fist word char count as it is 
            # since we have no thing to compare it to
            if index == 0:
                global_counter = counter
                continue
            
            for index, char_count_in_word in enumerate(counter):                
                global_counter[index] = min(global_counter[index], char_count_in_word)
        
        
        num_of_words = len(words)
        common = []
        for index, count in enumerate(global_counter):            
            char = chr(97 + index)
            for _ in range(count):
                common.append(char)
        
        return common
                    
        