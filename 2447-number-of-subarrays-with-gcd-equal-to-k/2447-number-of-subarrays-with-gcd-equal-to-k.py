class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        # bruteforce
        
        length = len(nums)
        
        count = 0
        
        for i in range(length):
            # gcd starting from index i to j
            
            current_gcd = nums[i]
            
            for j in range(i, length):
                
                current_gcd = gcd(current_gcd, nums[j])
            
                if current_gcd == k:
                    count += 1
                
                elif current_gcd < k:
                    break
        
        return count
                