class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater_map = {}
                
        for num in nums2:
            while stack and stack[-1] < num:                
                number = stack.pop()
                greater_map[number] = num
        
            stack.append(num)
        
        return map(lambda num: greater_map.get(num, -1), nums1)
        
        