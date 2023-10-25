class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        order_table = defaultdict(lambda: defaultdict(int))
        
        foods = set()
        
        for customer, table, food in orders:
            foods.add(food)
            order_table[int(table)][food] += 1
            
        
        header = ["Table"]                
        header.extend(food for food in sorted(foods))
                
        cols = len(header)
        
        display_table = [header]
        
        for table in sorted(order_table.keys()):
            
            row = ["0"] * cols
            
            for i, food in enumerate(header):                
                row[i] = str(order_table[table][food])
            
            row[0] = str(table)
            
            display_table.append(row)
    
        
        return display_table 