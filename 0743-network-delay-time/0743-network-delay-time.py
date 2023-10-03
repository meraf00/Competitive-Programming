class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        
        start_node = k - 1
        
        for i in range(n):
            dist[i][i] = 0
        
        for u, v, w in times:
            dist[u - 1][v - 1] = w
        
        for k in range(n):
            for u in range(n):
                for v in range(n):
                    dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])
        
        
        max_time = -float('inf')
        for time in dist[start_node]:
            if time == float('inf'):
                return -1
        
            max_time = max(max_time, time)
                        
        return max_time