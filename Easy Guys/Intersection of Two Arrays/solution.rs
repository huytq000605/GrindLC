impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        use std::collections::HashSet;
        let s: HashSet<i32> = nums1.into_iter().collect();
        let mut result = HashSet::<i32>::new();
        for num in nums2.iter() {
            if s.contains(num) {
                result.insert(*num);
            }
        }
        return result.into_iter().collect()
    }
}
