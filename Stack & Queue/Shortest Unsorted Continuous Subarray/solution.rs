impl Solution {
	pub fn find_unsorted_subarray(nums: Vec<i32>) -> i32 {
			let (mut left, mut right) = (0, 0);
			let n = nums.len();
			
			let mut prev = nums[0];
			for i in 0..n {
					if nums[i] >= prev {
							prev = nums[i];
					} else {
							right = i;
					}
			}
			
			prev = nums[n-1];
			for i in (0..n).rev() {
					if nums[i] <= prev {
							prev = nums[i];
					} else {
							left = i;
					}
			}
			
			if left == right {
					return 0
			}
			return (right - left + 1) as i32
	}
}