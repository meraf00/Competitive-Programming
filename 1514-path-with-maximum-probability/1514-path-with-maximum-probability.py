class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        
        for edge, prob in zip(edges, succProb):
            a, b = edge
            
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        
        
        heap = [(-1, start_node)]
        
        probs = [0] * n
        
        while heap:
            prob, node = heappop(heap)
            
            probs[node] = prob
            
            if node == end_node:
                break
            
            for nbr, nbr_prob in graph[node]:
                new_prob = prob * nbr_prob
                
                if new_prob < probs[nbr]:
                    heappush(heap, (new_prob, nbr))
        
            
        return -probs[end_node]
        