# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        
        def parent(j):
            return (j - 1) // 2

        def swap(heap,i, j):
            heap[i], heap[j] = heap[j], heap[i] 
            

        def heapify(arr):
            n = len(arr)
            
            for i in range(n // 2 - 1, -1, -1):
                heapify_down(arr, n, i)
        
        def heappush(heap, value):
            heap.append(value)
            currentIdx = len(heap) - 1
            heapify_up(heap, currentIdx)
        
        def heappop(heap):
            if not heap:
                return None

            min_value = heap[0]
            heap[0] = heap[-1]
            heap.pop()

            current = 0
            heapify_down(heap, len(heap), current) 

            return min_value
        
        def heapify_up(heap, j):
            p = parent(j)
            if j > 0 and heap[j].val < heap[p].val:
                swap(heap, j, p) 
                heapify_up(heap, p)        
        
        def heapify_down(heap, n, current_idx):
            small_child_idx = current_idx
            left_idx = 2 * current_idx + 1
            right_idx = 2 * current_idx + 2

            if left_idx < n and heap[left_idx].val < heap[small_child_idx].val:
                small_child_idx = left_idx 

            if right_idx < n and heap[right_idx].val < heap[small_child_idx].val:
                small_child_idx = right_idx

            if small_child_idx != current_idx:
                swap(heap, current_idx, small_child_idx)
                heapify_down(heap, n, small_child_idx)
                
        write = len(lists) - 1
        
        while lists[write] == None and write > -1:
            write -= 1
        
        if write == -1:
            return
        
        for i in range(len(lists)): 
            if i >= write:
                break
                
            if lists[i] == None:
                swap(lists, i, write)
                write -= 1                        
        
        
        while lists and not lists[-1]:
            lists.pop()
            
        
        
        dummy = ListNode()
        
        heapify(lists)
        
        current = dummy
        
        while lists:
            min_node = heappop(lists)
            
            if min_node:            
                current.next = min_node

                if min_node.next:            
                    heappush(lists, min_node.next)

                min_node.next = None
                current = current.next
        
        return dummy.next
            
        