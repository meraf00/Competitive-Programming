class Solution:
    def isNumber(self, s: str) -> bool:                
        try:             
            if s in ('inf', '+inf', '-inf', 'nan', 'Infinity', '-Infinity', '+Infinity'):
                return False
            
            float(s)
                
            return True
            
        except: return False
            