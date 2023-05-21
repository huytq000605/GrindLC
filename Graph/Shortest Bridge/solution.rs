use std::collections::VecDeque;

struct Pos {
  r: usize,
  c: usize,
}

impl Solution {
    pub fn shortest_bridge(mut grid: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (grid.len(), grid[0].len());
        let ds = vec![(1,0), (0,1), (-1,0), (0,-1)];
        let mut dq: VecDeque<Pos> = VecDeque::new();
        'first_island: for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    let (mut r, mut c) = (i, j);
                    let mut stack = vec![Pos{r: r, c: c}];
                    while stack.len() > 0 {
                        let pos = stack.pop().unwrap();
                        r = pos.r;
                        c = pos.c;
                        grid[r][c] = -1;
                        dq.push_back(Pos{r: r, c: c});
                        for (dr, dc) in ds.iter() {
                            let (nr, nc) = (r as i32 + dr, c as i32 + dc);
                            if nr < 0 || nc < 0 || nr >= m as i32 || nc >= n as i32 || grid[nr as usize][nc as usize] != 1 {
                                continue
                            }
                            let next_pos = Pos{r: nr as usize, c: nc as usize};
                            stack.push(next_pos);
                        }
                    }
                    break 'first_island;
                }
            }
        }
        let mut s = 0;
        while dq.len() > 0 {
            for _ in 0..dq.len() {
                let pos = dq.pop_front().unwrap();
                let r = pos.r;
                let c = pos.c;
                for (dr, dc) in ds.iter() {
                    let (nr, nc) = (r as i32 + dr, c as i32 + dc);
                    if nr < 0 || nc < 0 || nr >= m as i32 || nc >= n as i32 || grid[nr as usize][nc as usize] == -1 {
                        continue
                    }
                    if grid[nr as usize][nc as usize] == 1 {
                        return s
                    }
                    let next_pos = Pos{r: nr as usize, c: nc as usize};
                    grid[nr as usize][nc as usize] = -1;
                    dq.push_back(next_pos);
                }
            }
            s += 1;
        }
        return -1
    }
}
