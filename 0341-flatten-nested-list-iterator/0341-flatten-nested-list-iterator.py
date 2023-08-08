# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):                 
        self.nums = self.flatten(nestedList)        
        self.length = len(self.nums)
        
        self.current_index = 0
    
    
    def flatten(self, lst):
        output = []
        
        for item in lst:
            if item.isInteger():
                output.append(item.getInteger())
            else:
                output.extend(self.flatten(item.getList()))
        
        return output
    
    def next(self) -> int:
        value = self.nums[self.current_index]
        
        self.current_index += 1
        
        return value
    
    def hasNext(self) -> bool:
        return self.current_index < self.length
    
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())