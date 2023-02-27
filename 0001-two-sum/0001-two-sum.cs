public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> IndexMap = new Dictionary<int, int>();
        
        int[] result = {0, 0};
        
        for (int i=0; i < nums.Length; i++) {
            
            if (IndexMap.ContainsKey(target - nums[i])) {
                result[0] = IndexMap[target - nums[i]];
                result[1] = i;
                break;
            }
            
            IndexMap[nums[i]] = i;
        }
        
        return result;
    }
}