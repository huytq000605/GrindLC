impl Solution {
	pub fn backspace_compare(s: String, t: String) -> bool {
			let mut i: i32 = (s.len() - 1) as i32;
			let mut j: i32 = (t.len() - 1) as i32;
			while true {
					let mut back = 0;
					while i >= 0 && (s.chars().nth(i as usize).unwrap() == '#' || back > 0) {
							if s.chars().nth(i as usize).unwrap() == '#' {
									back += 1;
							} else {
									back -= 1;
							}
							i -= 1;
					}
					
					let mut back = 0;
					while j >= 0 && (t.chars().nth(j as usize).unwrap() == '#' || back > 0) {
							if t.chars().nth(j as usize).unwrap() == '#' {
									back += 1
							} else {
									back -= 1
							}
					j -= 1;
					};
					
					if i >= 0 && j >= 0 {
							if s.chars().nth(i as usize).unwrap() != t.chars().nth(j as usize).unwrap() {
									return false
							};
							i -= 1;
							j -= 1;
					} else {
							break;
					}
			};
			return (i == -1 && j == -1)
	}
}