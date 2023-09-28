class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n_cities = len(locations)
        
        dp = [[0] * n_cities for _ in range(fuel + 1)]
        
        dp[0][finish] = 1                
    
        for fuel in range(1, fuel + 1):
            for current_city in range(n_cities):
                if current_city == finish:
                    dp[fuel][current_city] += 1
                    
                for nbr_city in range(n_cities):
                    if nbr_city == current_city:
                        continue
                    
                    required_fuel = abs(locations[current_city] - locations[nbr_city])
                    
                    if required_fuel <= fuel:
                        dp[fuel][current_city] += dp[fuel - required_fuel][nbr_city]

        
        return dp[fuel][start] % (10**9 + 7)
        
            
        
        