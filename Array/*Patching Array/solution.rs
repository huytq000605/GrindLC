impl Solution {
	pub fn min_patches(nums: Vec<i32>, n: i32) -> i32 {
			let m = nums.len();
			let (mut result, mut idx, mut sum): (i32, usize, i64) = (0, 0, 0);
			while sum < (n as i64) {
					if idx < m && (nums[idx] as i64) <= sum + 1 {
							sum += nums[idx] as i64;
							idx += 1;
					} else {
							result += 1;
							sum += sum + 1;
					}
			}
			return result
	}
}