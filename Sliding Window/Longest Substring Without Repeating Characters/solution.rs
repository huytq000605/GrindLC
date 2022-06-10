impl Solution {
	pub fn length_of_longest_substring(s: String) -> i32 {
			let mut seen = std::collections::HashSet::new();
			let (mut result, mut start) = (0, 0);
			let bytes = s.as_bytes();
			for (i, b) in bytes.iter().enumerate() {
					while seen.contains(&b) {
							seen.remove(&bytes[start]);
							start += 1;
					}
					seen.insert(b);
					result = std::cmp::max(result, i - start + 1);
			}
			return result as i32
	}
}