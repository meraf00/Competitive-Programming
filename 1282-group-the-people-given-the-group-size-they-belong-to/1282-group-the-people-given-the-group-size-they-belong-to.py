class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # groupsize: [group members]
        groups = defaultdict(list)
        
        
        for person, size in enumerate(groupSizes):
            groups[size].append(person)
        
        
        answer = []
        
        for size, people  in groups.items():
            for i in range(0, len(people), size):
                answer.append(people[i:i+size])
        
        return answer
            
        
        
        