struct SegmentTree<T: Ord> {
	left: Option<Box<SegmentTree<T>>>,
	right: Option<Box<SegmentTree<T>>>,
	val: T,
	start: i32,
	end: i32,
	lazy: T
}

impl SegmentTree<i32> {
	fn new(start: i32, end: i32, val: i32) -> SegmentTree<i32> {
			SegmentTree {
					start: start,
					end: end,
					val: val,
					left: None,
					right: None,
					lazy: 0
			}
	}
	fn query(&mut self, start: i32, end: i32) -> i32 {
			if start > self.end || end < self.start {
					return 0
			}
			
			if start <= self.start && end >= self.end {
					return self.val
			}
			
			self.down();
			let left = match self.left {
					Some(ref mut left) => left.query(start, end),
					_ => panic!("crash and burn")
			};
			let right = match self.right {
					Some(ref mut right) => right.query(start, end),
					_ => panic!("crash and burn")
			};
			
			return std::cmp::max(left, right)
	}
	
	fn update(&mut self, start: i32, end: i32, val: i32) {
			if start > self.end || end < self.start {
					return
			}
			
			if start <= self.start && end >= self.end {
					self.val = val;
					self.lazy = val;
					return
			}
			
			self.down();
			let mut left = match self.left {
					Some(ref mut left) => left,
					_ => panic!("crash and burn")
			};
			let mut right = match self.right {
					Some(ref mut right) => right,
					_ => panic!("crash and burn")
			};
			left.update(start, end, val);
			right.update(start, end, val);
			self.val = std::cmp::max(left.val, right.val);
	}
	
	fn down(&mut self) {
			if self.start != self.end {
					match self.left {
							None => {
									let mid = self.start + (self.end - self.start) / 2;
									self.left = Some(Box::new(SegmentTree::new(self.start, mid, self.val)));
									self.right = Some(Box::new(SegmentTree::new(mid + 1, self.end, self.val)));
							},
							Some(ref mut left) => {
									if self.lazy > 0 {
											left.val = self.lazy;
											left.lazy = self.lazy;
											let right = match self.right {
													Some(ref mut right) => {
															right.val = self.lazy;
															right.lazy = self.lazy;
													},
													_ => panic!("crash and burn")
											};
									}
							}
					}
			}
			self.lazy = 0;
	}
}

impl Solution {
	pub fn falling_squares(positions: Vec<Vec<i32>>) -> Vec<i32> {
			let mut st = SegmentTree::new(0, 10i32.pow(14), 0);
			let mut result = vec![];
			for pos in positions {
					let (start, end) = (pos[0], pos[0] + pos[1] - 1);
					let value = pos[1];
					let cur = st.query(start, end);
					st.update(start, end, cur + value);
					result.push(st.val);
			}
			return result
	}
	
}