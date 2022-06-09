impl Solution {
	pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
			let (mut i, mut j) = (0, numbers.len() - 1);
			while i < j {
					if numbers[i] + numbers[j] == target {
							return vec![(i + 1) as i32, (j + 1) as i32]
					} else if numbers[i] + numbers[j] > target {
							j -= 1;
					} else {
							i += 1;
					}
			}
			return vec![]
	}
}