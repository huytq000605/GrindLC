impl Solution {
	pub fn min_swap(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
			let n = nums1.len();
			let mut swap = 1;
			let mut not_swap = 0;
			for i in 1..n {
					let (prev_swap, prev_not_swap) = (swap, not_swap);
					swap = n;
					not_swap = n;
					if nums1[i] > nums1[i-1] && nums2[i] > nums2[i-1] {
							swap = prev_swap + 1;
							not_swap = prev_not_swap;
					}
					
					if nums1[i] > nums2[i-1] && nums2[i] > nums1[i-1] {
							swap = std::cmp::min(swap, prev_not_swap + 1);
							not_swap = std::cmp::min(not_swap, prev_swap);
					}
			}
			return std::cmp::min(swap, not_swap) as i32
	}
}