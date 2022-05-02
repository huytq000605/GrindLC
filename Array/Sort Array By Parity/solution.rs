impl Solution {
	pub fn sort_array_by_parity(mut nums: Vec<i32>) -> Vec<i32> {
			let (mut i, mut j, n): (usize, usize, usize) = (0, 0, nums.len());
			while i < n {
					if nums[i] % 2 == 0 {
							nums.swap(i, j);
							j += 1;
					}
					i += 1;
			}
			return nums
	}
}