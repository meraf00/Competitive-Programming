class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(int)
        
        
        for src, dest in edges:
            graph[src] = max(0, graph[src])
            graph[dest] += 1
        
        
        vertices = []
        for node, count in graph.items():
            if count == 0:
                vertices.append(node)
        
        return vertices
        
            