impl Solution {
    pub fn max_chunks_to_sorted(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        let mut left_max = vec![arr[0]; n];
        let mut right_min = vec![arr[n-1]; n];
        let mut result = 1;
        
        for i in 1..n {
            left_max[i] = std::cmp::max(left_max[i-1], arr[i]);
        }
        
        for i in (0..n-1).rev() {
            right_min[i] = std::cmp::min(right_min[i+1], arr[i]);
        }
        
        for i in 0..n-1 {
            if left_max[i] <= right_min[i+1] {
                result += 1;
            }
        }
        return result
    }
}