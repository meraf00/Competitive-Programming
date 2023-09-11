use std::collections::HashMap;
use std::convert::TryInto;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen: HashMap<i32, i32> = HashMap::new();
        let mut answer: Vec<i32> = Vec::new();
        
        
        for (i, num) in nums.iter().enumerate() {            
            if (seen.contains_key(& (target - num))) {
                answer.push(i.try_into().unwrap());
                answer.push(
                    match seen.get(& (target - num)) {
                        Some(v) => *v,
                        None => *num
                    }
                );
                break;
            }
            
            seen.insert(*num, i.try_into().unwrap());
        }
        
        return answer;
    }
}