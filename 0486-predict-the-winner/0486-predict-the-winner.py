class Solution:
    def __init__(self):
        self.evaluated = {}
    
    def getScores(self, nums, turn=False, left=0, right=None):
        # turn [false] -> player1's turn                
        
        if right == None:
            right = len(nums) - 1
            
        if (left, right) in self.evaluated:
            return self.evaluated[(left, right)]
        
        if left == right:  
            score = [0, 0]
            score[turn] += nums[left]
            return score
                
        left_choosen = list(self.getScores(nums, not turn, left + 1, right))
        right_choosen = list(self.getScores(nums, not turn, left, right - 1))
              
        if left_choosen[turn] + nums[left] > right_choosen[turn] + nums[right]:
            left_choosen[turn] += nums[left]
            
            self.evaluated[(left, right)] = tuple(left_choosen)
            
            return left_choosen
            
        else:
            right_choosen[turn] += nums[right]
            
            self.evaluated[(left, right)] = tuple(right_choosen)
            
            return right_choosen
        
        
    def PredictTheWinner(self, nums: List[int]) -> bool:        
        player1, player2 = self.getScores(nums)
        
        return player1 >= player2
                  
       
        
        
        
        