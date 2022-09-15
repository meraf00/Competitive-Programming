"""
https://leetcode.com/problems/find-median-from-data-stream/
"""

import heapq
from typing import List

class MedianFinder:

    def __init__(self):
        self.data = []
        self.left = []
        self.right = []
        

    def addNum_(self, num: int) -> None:        
        if len(self.data) == 0:
            self.data.append(num)
            return
                
        low = 0
        high = len(self.data) - 1
        while low <= high:            
            mid = (low + high) // 2            
            if self.data[mid] < num:
                low = mid + 1
            elif self.data[mid] > num:
                high = mid - 1
            elif self.data[mid] == num:
                break   
        
        if num >= self.data[mid]:             
            self.data.insert(mid + 1, num)
        elif num > self.data[mid - 1] or mid == 0:
            self.data.insert(mid, num)
        else:
            self.data.insert(mid-1, num)
        
        
    def findMedian_(self) -> float:        
        size = len(self.data)        
        if size % 2 == 0:
            return (self.data[size//2 - 1] + self.data[size//2]) / 2
        return self.data[size//2]
    
    
    # Heap method
    def addNum(self, num: int) -> None:        
        heapq.heappush(self.right, num)
        val = heapq.heappop(self.right)
        heapq.heappush(self.left, -val)
        if len(self.right) < len(self.left):
            val = heapq.heappop(self.left)
            heapq.heappush(self.right, -val)
        
        
    def findMedian(self) -> float:                   
        if len(self.left) != len(self.right):
            return self.right[0]
        return (-self.left[0] + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()