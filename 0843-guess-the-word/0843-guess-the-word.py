# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def countMatch(self, word1, word2):
        count = 0
        
        for a, b in zip(word1, word2):
            if a == b:
                count += 1
            
        return count
    
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        n_words = len(words)
        
        # word : 
            # match (int 0-6): 
                # wordlist
                
        diff = defaultdict(lambda : defaultdict(set))
        
        for i in range(n_words):            
            word_i = words[i]
            
            for j in range(i, n_words):
                word_j = words[j]
                
                match = self.countMatch(word_i, word_j)
                
                diff[word_i][match].add(word_j)
                diff[word_j][match].add(word_i)
            
        
        # rank based on uniqueness of row
        rank_row = []
        for word in words:
            rank = len(diff[word])
            rank_row.append((-rank, word))
        
        heapify(rank_row)
        
        candidates = set(words)
                
        count = 0
        
        while rank_row:
            rank, word = heappop(rank_row)
            
            if word not in candidates:
                continue
            
            match = master.guess(word)
                        
            if match == 6:
                break
            
            candidates = candidates.intersection(diff[word][match])                        
            
"""
"ccoyyo"
["wichbx","oahwep","tpulot","eqznzs","vvmplb","eywinm","dqefpt","kmjmxr","ihkovg","trbzyb","xqulhc","bcsbfw","rwzslk","abpjhw","mpubps","viyzbc","kodlta","ckfzjh","phuepp","rokoro","nxcwmo","awvqlr","uooeon","hhfuzz","sajxgr","oxgaix","fnugyu","lkxwru","mhtrvb","xxonmg","tqxlbr","euxtzg","tjwvad","uslult","rtjosi","hsygda","vyuica","mbnagm","uinqur","pikenp","szgupv","qpxmsw","vunxdn","jahhfn","kmbeok","biywow","yvgwho","hwzodo","loffxk","xavzqd","vwzpfe","uairjw","itufkt","kaklud","jjinfa","kqbttl","zocgux","ucwjig","meesxb","uysfyc","kdfvtw","vizxrv","rpbdjh","wynohw","lhqxvx","kaadty","dxxwut","vjtskm","yrdswc","byzjxm","jeomdc","saevda","himevi","ydltnu","wrrpoc","khuopg","ooxarg","vcvfry","thaawc","bssybb","ccoyyo","ajcwbj","arwfnl","nafmtm","xoaumd","vbejda","kaefne","swcrkh","reeyhj","vmcwaf","chxitv","qkwjna","vklpkp","xfnayl","ktgmfn","xrmzzm","fgtuki","zcffuv","srxuus","pydgmq"]
10
"""       
        
        
                
            