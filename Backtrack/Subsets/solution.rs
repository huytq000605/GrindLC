impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result = vec![];
        for mask in 0..(1 << nums.len()) {
            let mut subset = vec![];
            for i in 0..nums.len() {
                if (mask >> i) & 1 == 1 {
                    subset.push(nums[i]);
                }
            }
            result.push(subset);
        }
        return result;
    }
}
