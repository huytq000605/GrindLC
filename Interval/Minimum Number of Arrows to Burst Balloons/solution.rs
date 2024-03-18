impl Solution {
    pub fn find_min_arrow_shots(points: Vec<Vec<i32>>) -> i32 {
        let mut sorted = points.clone();
        sorted.sort();
        let mut result = 1;
        let mut mx = sorted[0][1];
        for point in sorted[1..].iter() {
            match point[..] {
                [a, b] => {
                    if a > mx {
                        result += 1;
                        mx = b;
                    } else {
                        mx = std::cmp::min(mx, b);
                    }
                }
                _ => continue
            }
        }
        return result
    }
}
