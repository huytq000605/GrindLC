impl Solution {
    pub fn latest_day_to_cross(row: i32, col: i32, mut cells: Vec<Vec<i32>>) -> i32 {
        let (mut start, mut end) = (0, cells.len() as i32);
        cells = cells.into_iter().map(|mut cell| {
            cell[0] -= 1;
            cell[1] -= 1;
            cell
        }).collect();

        fn valid(m: i32, n: i32, cells: &Vec<Vec<i32>>, day: i32) -> bool {
            let ds = vec![(0,1), (1,0), (-1,0), (0,-1)];
            let mut dq = std::collections::VecDeque::new();
            let mut seen = std::collections::HashSet::new();
            for i in 0..day as usize {
                seen.insert((cells[i][0], cells[i][1]));
            }
            for col in 0..n {
                if !seen.contains(&(0, col)) {
                    seen.insert((0, col));
                    dq.push_back((0, col));
                }
            }
            while let Some((r, c)) = dq.pop_front() {
                if r == m-1 {
                    return true
                }
                for &(dr, dc) in ds.iter() {
                    let (nr, nc) = (r + dr, c + dc);
                    if nr < 0 || nc < 0 || nr >= m || nc >= n {
                        continue
                    }
                    if seen.contains(&(nr, nc)) {
                        continue
                    }
                    seen.insert((nr, nc));
                    dq.push_back((nr, nc));
                }
            }
            return false
        }

        while start < end {
            let mid = start + ((end - start + 1) as f64 / 2.0).ceil() as i32;
            if valid(row, col, &cells, mid) {
                start = mid;
            } else {
                end = mid - 1;
            }
        }
        return start
    }
}
