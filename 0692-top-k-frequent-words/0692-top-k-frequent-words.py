class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = Counter(words)
        
        words = list(map(lambda word: (-word_freq[word], word), set(words)))
        
        heapify(words)
        
        top_k = []
        while k > 0:
            top_k.append(heappop(words)[1])
            k -= 1
        
        return top_k
        
        
        
        
        