class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        files = defaultdict(int)            
        
        for idx, filename in enumerate(names):
            if filename not in files:
                files[filename] += 1
                continue
            
            count = files[filename]
            new_name = f'{filename}({count})'
            
            while new_name in files:
                count += 1
                new_name = f'{filename}({count})'
            
            names[idx] = new_name
            files[new_name] += 1
            files[filename] = files[new_name]
            
            
           
        return names
                
            