class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first_index_from_end = {}
        
        for index, char in enumerate(s):
            first_index_from_end[char] = index
        
        partition_lengths = []
        
        left = 0
        right = 0
        char = s[left]
        partition_right_bound = first_index_from_end[char]
        
        while right < len(s):
            if right >= partition_right_bound:
                length = partition_right_bound - left + 1
                partition_lengths.append(length)
                right += 1
                left = right 
                
                if left < len(s):
                    char = s[left]
                    partition_right_bound = first_index_from_end[char]
                continue
                
            char = s[right]
            new_bound = first_index_from_end[char]
            if new_bound > partition_right_bound:
                partition_right_bound = new_bound
                
            right += 1
        return partition_lengths
                