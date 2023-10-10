class Solution:
    def isIpv4(self, ip) -> bool:
        ip_list = ip.split('.')
        
        if len(ip_list) != 4:
            return False
        
        for x in ip_list:
            try:
                num = int(x)
                if str(num) != x:
                    return False
                
                if not 0 <= num <= 255:
                    return False
            
            except:
                return False
        
        return True
                
    
    def isIpv6(self, ip) -> bool:
        ip_list = ip.split(':')
        
        if len(ip_list) != 8:
            return False
        
        for x in ip_list:
            try:
                if not 1 <= len(x) <= 4:
                    return False
                
                int(x, 16)                                
            except:
                return False
        
        return True
                
        
        
    
    def validIPAddress(self, queryIP: str) -> str:
        
        if self.isIpv4(queryIP):
            return 'IPv4'
        
        elif self.isIpv6(queryIP):
            return 'IPv6'
        
        return 'Neither'