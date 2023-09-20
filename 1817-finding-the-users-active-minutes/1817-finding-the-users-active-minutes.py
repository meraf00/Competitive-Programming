class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        answer = [0] * k
        
        counter = defaultdict(set)
        
        for user, time in logs:
            counter[user].add(time)
        
        
        for user, times in counter.items():
            uam = len(times)
            
            if uam <= k:
                answer[uam - 1] += 1
        
        return answer
            
            