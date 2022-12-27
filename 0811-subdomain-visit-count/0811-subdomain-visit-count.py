class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_visit_count = defaultdict(int)
        
        for cpdomain in cpdomains:
            cpdomain = cpdomain.split()
            count = int(cpdomain[0])
            domain = cpdomain[1]
            
            domain_visit_count[domain] += count
            
            for index, char in enumerate(domain):
                if char == ".":
                    domain_substring = domain[index + 1:]
                    domain_visit_count[domain_substring] += count
        
        output = []
        for domain, visit_count in domain_visit_count.items():            
            output.append(f"{visit_count} {domain}")
        
        return output
                    
            
            
                    
            
        