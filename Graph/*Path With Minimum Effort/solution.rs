impl Solution {
    pub fn minimum_effort_path(heights: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (heights.len() as i32, heights[0].len() as i32);
        let mut efforts = vec![vec![i32::MAX; n as usize]; m as usize];
        efforts[0][0] = 0;
        let ds = vec![(0,1), (1,0), (-1,0), (0, -1)];
        let mut pq = std::collections::BinaryHeap::<(i32, i32, i32)>::new();
        pq.push((0, 0, 0));
        
        while let Some((e, r, c)) = pq.pop()  {
            if r == m - 1 && c == n - 1 {
                return -e
            }
            for (dr, dc) in ds.iter() {
                let (nr, nc) = (r + dr, c + dc);
                if nr < 0 || nc < 0 || nr >= m || nc >= n {
                    continue
                }
                let ne = std::cmp::max(-e, (heights[nr as usize][nc as usize] - heights[r as usize][c as usize]).abs());
                if efforts[nr as usize][nc as usize] > ne {
                    efforts[nr as usize][nc as usize] = ne;
                    pq.push((-ne, nr, nc));
                } 
            }
        }
        return -1
    }
}
