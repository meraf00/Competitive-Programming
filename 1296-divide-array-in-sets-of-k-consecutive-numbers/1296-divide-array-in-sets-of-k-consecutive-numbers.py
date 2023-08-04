class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:        
        seqs = defaultdict(list)        
        
        nums.sort()
        
        for num in nums:
            list_of_seq = seqs[num - 1]        
            
            # get the shortest seq ending with num-1 
            # and append num (-num) to maintain heap structure sorted by length
            if list_of_seq and len(list_of_seq[0]) < k:
                seq = heappop(list_of_seq)
                seq.append(-num)
            
            else:
                seq = [-num]
                
            heappush(seqs[num], seq)
                    
        for sequences in seqs.values():
            for seq in sequences:
                if len(seq) != k:
                    return False
            
        return True
                    
                    
                
            
            
                