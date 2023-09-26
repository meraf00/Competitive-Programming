class TrieNode:
    def __init__(self, name=""):
        self.children = defaultdict(lambda : TrieNode())
        self.is_end = False
        
        self.name = name

        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, path):
        current = self.root
        
        for folder in path:
            current = current.children[folder]
            
            if current.is_end:
                break
        
        current.is_end = True
        
        current.children = {}  
    
    def get_folders(self):
        folders = []
        
        stack = [(self.root, '')]
        
        while stack:
            current, path = stack.pop()
            
            if current.is_end:
                folders.append(path)
        
            for folder_name, node in current.children.items():
                stack.append((node, path + '/' + folder_name))
        
        return folders
    
    

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        
        for path_string in folder:
            path = path_string[1:].split('/')
            
            trie.insert(path)
        
        return trie.get_folders()
        
