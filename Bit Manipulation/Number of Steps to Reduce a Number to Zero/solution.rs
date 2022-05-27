impl Solution {
	pub fn number_of_steps(mut num: i32) -> i32 {
		if num == 0 {
				return 0
		}
		let mut result = 0;
		while num > 0 {
			if num % 2 == 1 {
				result += 2;
			} else {
				result += 1;
			}
			num >>= 1;
		}
		return result - 1
	}
}