class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        sequence_map = defaultdict(list)
        
        for num in nums:
            if not sequence_map[num - 1]:
                heappush(sequence_map[num], 1)
            else:
                min_seq_length = heappop(sequence_map[num - 1])
                heappush(sequence_map[num], min_seq_length + 1)
        
        for sequence_length_list in sequence_map.values():
            if sequence_length_list:
                # since the list is heapified list[0] is minimum
                if sequence_length_list[0] < 3:
                    return False
        
        return True
                