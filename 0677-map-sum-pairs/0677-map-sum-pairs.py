class MapSum:

    def __init__(self):
        self.map_sum = defaultdict(int)
        self.key_value = defaultdict(int)

    def insert(self, key: str, val: int) -> None:        
        for i in range(1, len(key) + 1):
            self.map_sum[key[:i]] += val - self.key_value[key]
                
        self.key_value[key] = val
        

    def sum(self, prefix: str) -> int:        
        return self.map_sum[prefix]
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)