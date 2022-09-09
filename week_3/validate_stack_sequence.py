from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushIndex = 0
        popIndex = 0

        stack = []

        while pushIndex < len(pushed):
            stack.append(pushed[pushIndex])
            while len(stack) and stack[-1] == popped[popIndex]:
                stack.pop()
                popIndex += 1

            pushIndex += 1

        while len(stack):
            if stack.pop() != popped[popIndex]:
                return False
            popIndex += 1

        return len(stack) == 0 and popIndex == len(popped) == pushIndex