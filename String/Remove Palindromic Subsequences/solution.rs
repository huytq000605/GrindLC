impl Solution {
	pub fn remove_palindrome_sub(s: String) -> i32 {
			if s.len() == 0 {
					return 0
			}
			let bytes = s.as_bytes();
			let mut is_palindrome = true;
			let (mut i, mut j) = (0, s.len() - 1);
			while i < j {
					if bytes[i] != bytes[j] {
							is_palindrome = false;
							break
					}
					i += 1;
					j -= 1;
			}
			if is_palindrome {
					return 1
			} else {
					return 2
			}
	}
}