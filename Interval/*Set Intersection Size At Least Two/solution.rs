impl Solution {
	pub fn intersection_size_two(mut intervals: Vec<Vec<i32>>) -> i32 {
			intervals.sort_by_key(|interval| (interval[1], -interval[0]));
			let (mut last, mut second) = (-1, -1);
			let mut result = 0;
			for interval in &intervals {
					let (a, b) = (interval[0], interval[1]);
					if a > last {
							result += 2;
							last = b;
							second = b-1;
					} else if a > second {
							result += 1;
							second = last;
							last = b;
					}
			}
			return result;
	}
}