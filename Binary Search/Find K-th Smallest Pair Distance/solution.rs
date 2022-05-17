impl Solution {
	pub fn smallest_distance_pair(mut nums: Vec<i32>, k: i32) -> i32 {
			nums.sort();
			let n = nums.len();
			let (mut start, mut end) = (0, nums[n-1] - nums[0]);
			while start < end {
					let mid = start + (end - start) / 2;
					let (mut i, mut j, mut count) = (0, 0, 0);
					while i < n {
							while j < n && nums[j] - nums[i] <= mid {
									j += 1;
							}
							count += j - i - 1;
							i += 1;
					}
					if (count as i32) < k {
							start = mid + 1;
					} else {
							end = mid;
					}
			}
			return start
	}
}