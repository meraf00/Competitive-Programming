class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        is_palindrom = defaultdict(bool)
        
        count = 0
        
        for i in range(n):
            is_palindrom[(i, i)] = True
            count += 1
                        
        for gap in range(2, n + 1):
            for start in range(0, n - gap + 1):
                end = start + gap - 1
                
                if gap == 2:
                    if s[start] == s[end]:
                        is_palindrom[(start, end)] = True
                        count += 1
                        
                else:
                    if s[start] == s[end] and is_palindrom[(start + 1, end - 1)]:
                        is_palindrom[(start, end)] = True
                        count += 1
        
        return count
                        
                    