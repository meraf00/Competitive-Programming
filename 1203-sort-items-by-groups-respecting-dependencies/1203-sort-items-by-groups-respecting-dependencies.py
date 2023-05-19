class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        items_graph = defaultdict(list)
        
        group_graph = defaultdict(list)
        
        indegrees_items = defaultdict(int)
        
        indegrees_groups = defaultdict(int)     
                
        # to create group for ungrouped        
        for i in range(len(group)):
            if group[i] == -1:
                group[i] = m
                m += 1
        
        for node, prereq in enumerate(beforeItems):
            node_group = group[node]
            
            for pn in prereq:
                items_graph[pn].append(node)
                indegrees_items[node] += 1
                
                ns_group = group[pn]                
                
                if ns_group != node_group:
                    group_graph[ns_group].append(node_group)
                    indegrees_groups[node_group] += 1
            
        
        
#         print(indegrees_items)
#         print(items_graph)
        
#         print(indegrees_groups)
#         print(group_graph)
        
        
        # determine group order and also check if it has cycle        
        group_order = []
        
        queue = deque()
        for grp in range(m):
            if indegrees_groups[grp] == 0:
                queue.append(grp)                
        
        
        while queue:
            current = queue.popleft()
            
            group_order.append(current)
            
            for nbr in group_graph[current]:
                indegrees_groups[nbr] -= 1
                
                if indegrees_groups[nbr] == 0:
                    queue.append(nbr)
        
        if len(group_order) < m:
            return []
        
        
        items_order = []
        
        queue = deque()
        for item in range(n):
            if indegrees_items[item] == 0:
                queue.append(item)
                
                                    
        while queue:
            current = queue.popleft()

            items_order.append(current)

            for nbr in items_graph[current]:
                indegrees_items[nbr] -= 1

                if indegrees_items[nbr] == 0:
                    queue.append(nbr)
                
        if len(items_order) < n:
            return []
                
        
        # group : items ordered
        all_order = defaultdict(list)
        
        for item in items_order:
            item_group = group[item]
            all_order[item_group].append(item)
            
        
        actual_order = []
        
        for grp in group_order:            
            actual_order.extend(all_order[grp])
        
        
        return actual_order