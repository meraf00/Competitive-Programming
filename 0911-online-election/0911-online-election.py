class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        
        counter = defaultdict(int)
        
        current_winner = self.persons[0]
        
        for index, person in enumerate(persons):             
            counter[person] += 1
            
            if counter[person] >= counter[current_winner]:
                current_winner = person

            self.persons[index] = current_winner        
                        
        

    def q(self, t: int) -> int:
        index = bisect_left(self.times, t)
        
        if index >= len(self.times) or (index < len(self.times) and self.times[index] > t):
            index = index - 1
        
        return self.persons[index]



# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)