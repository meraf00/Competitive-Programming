class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for a, b in richer:
            graph[a].append(b)
            indegree[b] += 1
        
        
        # (person, quiter_person)
        queue = deque()
        
        for node in graph.keys():
            if indegree[node] == 0:
                queue.append(node)
                
          
        answer = [i for i in range(len(quiet))]
                        
        while queue:               
            person = queue.popleft()  
            
            quieter_person = answer[person]
            quieter_person_quietness = quiet[quieter_person]
            
            
            
            for nbr in graph[person]:                
                indegree[nbr] -= 1
                
                nbr_quietness = quiet[answer[nbr]]
                                
                    
                if nbr_quietness >= quieter_person_quietness:
                    answer[nbr] = quieter_person
                    

                if indegree[nbr] == 0:
                    queue.append(nbr)
                    
                    
        
        return answer
            
            