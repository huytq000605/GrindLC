impl Solution {
    pub fn permute(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        let (mut result, mut cur) = (vec![], vec![]);
        fn dfs(i: usize, result: &mut Vec<Vec<i32>>, cur: &mut Vec<i32>, nums: &mut Vec<i32>) {
            if i >= nums.len() {
                result.push(cur.clone());
                return
            }
            for j in i..nums.len() {
                cur.push(nums[j]);
                nums.swap(i, j);
                dfs(i+1, result, cur, nums);
                cur.pop();
                nums.swap(i, j);
            }
        }
        dfs(0, &mut result, &mut cur, &mut nums);
        result
    }
}
