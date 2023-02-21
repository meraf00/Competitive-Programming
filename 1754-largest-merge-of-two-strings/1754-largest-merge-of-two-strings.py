class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        index_1 = 0
        index_2 = 0
        
        len_1 = len(word1)
        len_2 = len(word2)
        
        ans = []
        while index_1 < len_1 and index_2 < len_2:
            if word1[index_1:] > word2[index_2:]:
                char = word1[index_1]
                index_1 += 1
            else:
                char = word2[index_2]
                index_2 += 1
            
            ans.append(char)

        if index_1 < len_1:
            ans.append(word1[index_1:])
        if index_2 < len_2:
            ans.append(word2[index_2:])
        
        return "".join(ans)
                
        
        