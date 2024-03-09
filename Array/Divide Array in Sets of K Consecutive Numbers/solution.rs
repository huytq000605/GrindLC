impl Solution {
    pub fn is_possible_divide(nums: Vec<i32>, k: i32) -> bool {
        let mut counter = std::collections::HashMap::<i32, i32>::new();
        for num in nums.iter() {
            counter.entry(*num).
                and_modify(|freq| *freq += 1).
                or_insert(1);
        }
        let mut dq = std::collections::VecDeque::<i32>::new();
        let (mut sets, mut prev_num) = (0, -1);
        let mut sorted_map: Vec<_> = counter.iter().collect();
        sorted_map.sort_by(|a, b| a.0.partial_cmp(b.0).unwrap());
        for (&num, &freq) in sorted_map.into_iter() {
            if (freq < sets) || (sets > 0 && num - 1 > prev_num) {
                return false
            }
            dq.push_back(freq - sets);
            prev_num = num;
            sets = freq;
            if dq.len() == k as usize {
                sets -= dq.pop_front().unwrap();
            }
        }
        return sets == 0
    }
}
