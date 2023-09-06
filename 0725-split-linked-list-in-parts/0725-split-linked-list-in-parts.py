# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        node_count = 0
        
        current = head        
        while current:
            node_count += 1
            current = current.next
        
        nodes_per_part = node_count // k
        remainder_count = node_count % k
        
        
        answer = [None] * k
        
        current = head
        part_root = head
        counter = 0
        i = 0
        while current:             
            counter += 1
            
            if remainder_count > 0:
                required_part_length = nodes_per_part + 1
            else:
                required_part_length = nodes_per_part
            
            if counter == required_part_length:
                answer[i] = part_root
                temp = current
                
                part_root = current.next
                current = current.next
                temp.next = None
                
                i += 1
                counter = 0
                remainder_count -= 1
                
                continue
            
            current = current.next
        
        return answer
            
                