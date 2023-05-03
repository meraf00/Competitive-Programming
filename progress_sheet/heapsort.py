#User function Template for python3

class Solution:
    def heappop(self, heap):
        min_val = heap[0]
    
        heap[0] = heap[-1]
        heap.pop()  
    
        self.down_heap(heap, 0)  
            
        return min_val

    # min heap
    def down_heap(self, heap, index):
        length = len(heap)
    
        current = index
        
        while current < length:
            min_child = current
            left = 2 * current + 1
            right = 2 * current + 2
                   
            if left < length and heap[left] < heap[min_child]:
                min_child = left
    
            if right < length and heap[right] < heap[min_child]:
                min_child = right
            
    
            if current == min_child:
                break
    
            heap[current], heap[min_child] = heap[min_child], heap[current]
    
            current = min_child
    
    #Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        for i in range(len(arr) - 1, -1, -1):
            self.down_heap(arr, i)
        
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        self.heapify(arr, 0, 0)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr, 0)
        sorted_ = []
        
        while arr:
            sorted_.append(self.heappop(arr))
        
        for n in sorted_:
            arr.append(n)
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends