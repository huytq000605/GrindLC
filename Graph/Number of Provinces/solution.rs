struct UF {
    p: Vec<usize>,
    r: Vec<usize>
}

impl UF {
    pub fn new(n: usize) -> Self {
        UF {
            p: vec![0; n].iter().enumerate().map(|(i, _)| i).collect(),
            r: vec![0; n]
        }
    }

    pub fn find(&mut self, u: usize) -> usize {
        if u != self.p[u] {
            self.p[u] = self.find(self.p[u]);
        }
        return self.p[u]
    }

    pub fn union(&mut self, u: usize, v: usize) -> bool {
        let (mut u, mut v) = (self.find(u), self.find(v));
        if u == v { return false }
        if self.r[u] < self.r[v] {
            std::mem::swap(&mut u, &mut v);
        }
        self.p[v] = u;
        self.r[u] += self.r[v];
        return true
    }
}

impl Solution {
    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
        let n = is_connected.len();
        let mut result = n;
        let mut uf = UF::new(n);
        for i in 0..n {
            for j in i+1..n {
                if is_connected[i][j] == 1 && uf.union(i, j) {
                    result -= 1;
                }
            }
        }
        return result as i32
    }
}
