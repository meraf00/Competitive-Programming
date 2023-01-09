class Solution:
    def minOperations(self, boxes: str) -> List[int]: 
        
        balls_to_right = 0
        operations = 0
        
        # calculate the total number of balls and 
        # total number of operations to put them in the first box
        for index, box in enumerate(boxes):
            if box == "1":
                balls_to_right += 1
                operations += index
                 
        balls_to_left = 0        
        output = [operations] * len(boxes)                
        
        # whenever we move to the right we are decreasing the number of 
        # operations for the left balls by 1 (for each)
        # while increasing by 1 for each right ball
        for index, box in enumerate(boxes[:-1]):
            if box == "1":
                balls_to_right -= 1
                balls_to_left += 1
            
            operations -= balls_to_right
            operations += balls_to_left
            
            output[index + 1] = operations                    
        
        return output
                
                
        