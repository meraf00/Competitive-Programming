from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		def has_cycle(node, parent):
		    for nbr in adj[node]:
		        if nbr in visited and nbr != parent:
		            return True
		           
		        if nbr != parent:
		            visited.add(nbr)
		            if has_cycle(nbr, node):
		                return True
		    return False
		        
		visited = set()
		for node in range(V):
		    if node not in visited:
    		    if has_cycle(node, None):
    		        return True
		 
		return False


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends