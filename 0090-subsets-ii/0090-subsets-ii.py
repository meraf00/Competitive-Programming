class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n_nums = len(nums)
        
        subset_hashes = set()
        
        subsets = []
        
        current = []
        
        def _hash(subset):
            count = [0] * 21
            
            for num in subset:
                count[num] += 1            
            
            return '_'.join(map(str, count))
                
        
        def backtrack(idx):
            if idx >= n_nums:
                subset_id = _hash(current)
                if subset_id not in subset_hashes:
                    subsets.append(current[:])   
                    subset_hashes.add(subset_id)
                
                return
            
            
            current.append(nums[idx])
            backtrack(idx + 1)
            current.pop()
            
            backtrack(idx + 1)
            
            
        backtrack(0)        
        
        return subsets