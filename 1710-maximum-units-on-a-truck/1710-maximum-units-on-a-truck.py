class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box: box[1], reverse=True)
        
        total_units = 0
        
        for n_boxes, unit_per_box in boxTypes:
            if truckSize <= 0:
                break
                
            if n_boxes <= truckSize:
                truckSize -= n_boxes                
                total_units += unit_per_box * n_boxes
            
            else:                
                total_units += unit_per_box * truckSize
                truckSize = 0            
            
            
            
        return total_units
                
            
            
                
                
            
            
            
            