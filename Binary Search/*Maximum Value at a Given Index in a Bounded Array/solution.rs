impl Solution {
    pub fn max_value(n: i32, index: i32, mut max_sum: i32) -> i32 {
        max_sum -= n;
        let index = index as i64;
        let n = n as i64;
        let (mut start, mut end) = (0 as i64, max_sum as i64);
        while start < end {
            let num = start + ((end - start + 1) as f64 / 2.0).ceil() as i64;
            let left_num = std::cmp::max(0, num - index);
            let left = (num + left_num) * (num - left_num + 1) / 2 - num;
            let right_num = std::cmp::max(0, num - (n - 1 - index));
            let right = (num + right_num) * (num - right_num + 1) / 2 - num;
            if left + num + right > max_sum as i64 {
                end = num - 1;
            } else {
                start = num;
            }
        }
        return start as i32 + 1;
    }
}
