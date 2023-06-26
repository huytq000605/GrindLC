use std::collections::BinaryHeap;

impl Solution {
    pub fn total_cost(costs: Vec<i32>, mut k: i32, candidates: i32) -> i64 {
        let n = costs.len() as i32;
        let (mut first, mut last): (BinaryHeap<i32>, BinaryHeap<i32>) = (BinaryHeap::new(), BinaryHeap::new());
        for i in 0..candidates as usize {
            first.push(-costs[i as usize]);
        }
        for i in std::cmp::max((n-candidates), candidates) as usize..n as usize {
            last.push(-costs[i])
        }
        let (mut i, mut j) = (candidates, (n-1-candidates));
        let mut result: i64 = 0;
        while k > 0 {
            if last.len() == 0 || (first.len() > 0 && -first.peek().unwrap() <= -last.peek().unwrap()) {
                result -= first.pop().unwrap() as i64;
                if i <= j {
                    first.push(-costs[i as usize]);
                    i += 1;
                }
            } else {
                result -= last.pop().unwrap() as i64;
                if i <= j {
                    last.push(-costs[j as usize]);
                    j -= 1;
                }
            }
            k -= 1;
        }
        return result
    }
}
