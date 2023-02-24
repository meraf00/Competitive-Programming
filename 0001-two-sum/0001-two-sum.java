class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = {0, 0};
        
        outer:
        for (int i=0; i < nums.length; i++) {
            for (int j = i+1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target ){
                    result[0] = i;
                    result[1] = j;
                    break outer;
                }
            }
        }
        
        return result;   
    }
}