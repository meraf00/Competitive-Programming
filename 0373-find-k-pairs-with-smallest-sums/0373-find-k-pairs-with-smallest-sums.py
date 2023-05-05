class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        length_1 = len(nums1)
        length_2 = len(nums2)
        
        output = []
        
        heap = [(nums1[0] + nums2[0], 0, 0)]
        
        seen = set()
        
        while heap and len(output) < k:
            
            _sum, idx1, idx2 = heappop(heap)
            
            output.append([nums1[idx1], nums2[idx2]])
            
            if idx1 + 1 < length_1 and (idx1 + 1, idx2) not in seen:
                heappush(heap, (nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2))
                seen.add((idx1 + 1, idx2))
                
            
            if idx2 + 1 < length_2 and (idx1, idx2 + 1) not in seen:
                heappush(heap, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))
                seen.add((idx1, idx2 + 1))
        
    
        return output
        
                
                
            
            
        