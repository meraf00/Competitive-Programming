"""
https://leetcode.com/problems/merge-k-sorted-lists/
"""

import heapq
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class ComparableListNode(ListNode):
    def __init__(self, listnode):        
        self.val = listnode.val
        self.next = None
        
        if listnode.next:
            self.next = ComparableListNode(listnode.next)        
       
    def __lt__(self, listnode):
        return self.val < listnode.val
    def __gt__(self, listnode):
        return self.val > listnode.val
    
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        i = 0
        while i < len(lists):
            if lists[i] == None:
                del lists[i]
                continue
            i += 1
        lists = list(map(ComparableListNode, lists))
        
        heapq.heapify(lists)
        
        merged = None         
        
        while len(lists):
            min_node = heapq.heappop(lists)            
            if merged:
                merged_tail.next = min_node
                merged_tail = merged_tail.next
            else:
                merged = min_node
                merged_tail = merged
            
            if min_node.next:
                heapq.heappush(lists, min_node.next)
            
        return merged