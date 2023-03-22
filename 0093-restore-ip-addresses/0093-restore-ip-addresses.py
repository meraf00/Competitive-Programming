class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        length = len(s)
        
        possible_ips = []
        
        current = []
        
        def backtrack(start_index):
            if len(current) > 4: 
                return
            
            if start_index >= length:
                if len(current) == 4:
                    possible_ips.append(".".join(current))
                    
                
            
            for i in range(start_index, length):
                group = s[start_index: i + 1]
                
                if len(group) > 1 and group[0] == "0":
                    continue
                
                if len(group) > 3 or not (0 <= int(group) <= 255):
                    continue
                    
                current.append(group)
                
                backtrack(i + 1)
                
                current.pop()
        
        
        backtrack(0)
        
        return possible_ips
        