class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = set()
        for u, v in edges:
            if u in seen:
                return u
            if v in seen:
                return v
            seen.add(u)
            seen.add(v)