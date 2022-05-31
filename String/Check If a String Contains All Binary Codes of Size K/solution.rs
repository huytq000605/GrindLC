impl Solution {
	pub fn has_all_codes(s: String, k: i32) -> bool {
			let k = k as usize;
			let n = s.len();
			if n < k {
					return false
			}
			let goal: usize = 1 << k;
			let mut binary = 0;
			let bytes = s.as_bytes();
			let mut seen = std::collections::HashSet::new();
			for i in (0..k) {
					binary <<= 1;
					let last_bit = match (bytes[i] as char).to_digit(10) {
							Some(bit) => bit as usize,
							None => return false,
					};
					binary |= last_bit;
			}
			seen.insert(binary);
			for i in (k..n) {
					binary <<= 1;
					binary &= !goal;
					let last_bit = match (bytes[i] as char).to_digit(10) {
							Some(bit) => bit as usize,
							None => return false,
					};
					binary |= last_bit;
					seen.insert(binary);
					if seen.len() == goal {
							return true
					}
			}
			return false
	}
}