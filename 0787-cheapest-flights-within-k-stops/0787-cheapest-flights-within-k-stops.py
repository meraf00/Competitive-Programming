class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        
        for start, end, price in flights:
            graph[start].append((end, price))
        
        
        dp = [[float('inf')] * n for _ in range(k + 2)]
        
        for row in dp:
            row[src] = 0
        
        for curr_k in range(1, k + 2):
            for node in range(n):
                for nbr, price in graph[node]:
                    dp[curr_k][nbr] = min(dp[curr_k - 1][nbr], dp[curr_k - 1][node] + price, dp[curr_k][nbr])
        
        
        if dp[-1][dst] == float('inf'):
            return -1
        
        return dp[-1][dst]
            