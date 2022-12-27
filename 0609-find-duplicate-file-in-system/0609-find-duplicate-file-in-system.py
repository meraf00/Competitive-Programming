class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)
        for path_content in paths:
            
            to_list = path_content.split(" ")
            
            root = to_list[0]
            
            files_with_content = to_list[1:]
            
            for file in files_with_content:
                idx = file.index("(")
                file_name = file[:idx]
                content = file[idx+1:-1]
                content_map[content].append(root + "/" + file_name)
        
        output = []
        for filenames in content_map.values():
            if len(filenames) > 1:
                output.append(filenames)
        return output
        
        
                
        