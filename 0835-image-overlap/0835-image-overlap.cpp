class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        int max_overlap = 0;
        
        int rows = img1.size();
        int cols = img1[0].size();                
        
        int overlaps = 0; 
        
   
            
        for (int dx = -rows + 1; dx < rows; dx++) {
            for (int dy = -cols + 1; dy < cols; dy++) {
                
                overlaps = 0;                              
                
                for (int r=0; r<rows; r++) {
                    for (int c=0; c<cols; c++) {
                        if (0 <= r - dy && r - dy < rows && 0 <= c - dx && c - dx < cols)  {
                            if ((img1[r - dy][c - dx] == img2[r][c]) && (img2[r][c] == 1)) {
                                overlaps += 1;
                            }                           
                        }
                             
                    }
                }       
                
            max_overlap = max(max_overlap, overlaps);          
            }
        }
            
        return max_overlap;
    }
};