class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        sorted_by_freq = Counter(nums).most_common()
        
        max_freq = sorted_by_freq[0][1]
        
        result = [[] for _ in range(max_freq)]
        
        for num, freq in sorted_by_freq:
            for i in range(freq):
                result[i].append(num)                
                
        return result
    