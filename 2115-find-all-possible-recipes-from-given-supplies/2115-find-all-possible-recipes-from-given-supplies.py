class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        
        indegree = defaultdict(int)
        
        for idx, recipe in enumerate(recipes):
            for ingredient in ingredients[idx]:                
                graph[ingredient].append(recipe)
            
            indegree[recipe] = len(ingredients[idx])
                    
        queue = deque(supplies)
        
        makeable = set()
        
        while queue:
            current = queue.popleft()
            
            makeable.add(current)
            
            for nbr in graph[current]:
                indegree[nbr] -= 1
                
                if indegree[nbr] == 0:
                    queue.append(nbr)
        
        return list(makeable.intersection(recipes))
            
            
        
            