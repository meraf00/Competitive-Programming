function twoSum(nums: number[], target: number): number[] {
    let indexMap = {};
    
    for (let i=0; i < nums.length; i++) {
        
        if (indexMap[target - nums[i]] !== undefined) {
            return [i, indexMap[target - nums[i]]]
        }
        indexMap[nums[i]] = i;        
    }
        

};