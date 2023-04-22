class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        ans = [0] * len(labels)
        def dfs(node, visited):                        
            # leaf node
            if len(graph[node]) == 1 and graph[node][0] in visited:
                ans[node] = 1
                count = defaultdict(int)
                count[labels[node]] = 1
                return count
            
            current_count = defaultdict(int)            
            for child in graph[node]:
                if child in visited:
                    continue
                
                visited.add(child)
                for node_label, count in dfs(child, visited).items():
                    current_count[node_label] += count
                visited.remove(child)
            
            current_count[labels[node]] += 1
            ans[node] = current_count[labels[node]]
            
            return current_count
        
        dfs(0, set([0]))
        
        return ans