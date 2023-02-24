class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater_map = {}
                
        for i, num in enumerate(nums2):
            while stack and nums2[stack[-1]] < num:
                index = stack.pop()
                number = nums2[index]
                greater_map[number] = num
        
            stack.append(i)
        
        answer = []
        for num in nums1:
            greater = greater_map.get(num, -1)
            answer.append(greater)
        
        return answer
            
        