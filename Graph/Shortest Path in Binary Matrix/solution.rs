use std::collections::VecDeque;

impl Solution {
    pub fn shortest_path_binary_matrix(mut grid: Vec<Vec<i32>>) -> i32 {
        if grid[0][0] == 1 {
            return -1
        }
        let (m, n) = (grid.len() as i32, grid[0].len() as i32);
        let ds = vec![(1,0), (0,1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)];
        let mut dq: VecDeque<(i32, i32, i32)> = VecDeque::new();
        dq.push_back((1, 0, 0));
        while dq.len() > 0 {
            let (s, r, c) = dq.pop_front().unwrap();
            if r == (m-1) && c == (n-1) {
                return s
            }
            for (dr, dc) in ds.iter() {
                let (nr, nc) = (r + dr, c + dc);
                if nr < 0 || nc < 0 || nr >= m || nc >= n {
                    continue
                }
                if grid[nr as usize][nc as usize] == 1 {
                    continue
                }
                grid[nr as usize][nc as usize] = 1;
                dq.push_back((s + 1, nr, nc));
            }
        }
        return -1
    }
}
