impl Solution {
    pub fn is_majority_element(nums: Vec<i32>, target: i32) -> bool {
        fn binary_search(nums: &Vec<i32>, target: i32) -> usize {
            let (mut start, mut end) = (0, nums.len());
            while start < end {
                let mid = start + (end - start) / 2;
                if nums[mid] < target {
                    start = mid + 1;
                } else {
                    end = mid;
                }
            }
            return start
        }
        return binary_search(&nums, target+1) - binary_search(&nums, target) > nums.len() / 2
        
    }
}
