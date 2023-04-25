
class ThroneInheritance:

    def __init__(self, kingName: str):        
        self.family_tree = defaultdict(list)
        self.family_tree[kingName] = []
        self.king_name = kingName
        self.dead = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        self.family_tree[parentName].append(childName)                    

    def death(self, name: str) -> None:
        self.dead.add(name)        

    def getInheritanceOrder(self) -> List[str]:
        inheritance_order = []
        
        def preorder(parent):
            if parent not in self.dead:
                inheritance_order.append(parent)
            
            for child in self.family_tree[parent]:
                preorder(child)
        
        preorder(self.king_name)
        
        return inheritance_order
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()