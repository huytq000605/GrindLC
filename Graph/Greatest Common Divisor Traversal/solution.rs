struct UF {
    p: Vec<usize>,
    r: Vec<usize>
}

impl UF {
    fn new(n: usize) ->  Self {
        let mut p = vec![0; n];
        let r = vec![1; n];
        for i in 0..n {
            p[i] = i;
        }
        return UF{
            p: p,
            r: r
        }
    }

    fn find(&mut self, u: usize) -> usize {
        if u != self.p[u] {
            self.p[u] = self.find(self.p[u]); 
        }
        return self.p[u]
    }

    fn union(&mut self, u : usize, v: usize) {
        let (u, v) = (self.find(u), self.find(v));
        if u == v {return}
        if self.r[u] < self.r[v] {
            let (u, v) = (v, u);
        }
        self.r[u] += self.r[v];
        self.p[v] = u;
    }

    fn rank(&mut self, u: usize) -> usize {
        let p = self.find(u);
        return self.r[p]
    }
}

impl Solution {
    pub fn can_traverse_all_pairs(nums: Vec<i32>) -> bool {
        let n = nums.len();
        if n == 1 {
            return true
        }
        use std::collections::HashMap;
        let mut factors: HashMap<i32, usize> = HashMap::new();
        let mut uf = UF::new(n);
        for (i, num_ptr) in nums.iter().enumerate() {
            let mut num = *num_ptr;
            if num == 1 {
                return false
            }
            let mut f = 2;
            while f * f <= num {
                if num % f == 0 {
                    if factors.contains_key(&f) {
                        uf.union(*factors.get(&f).unwrap(), i);
                    } else {
                        factors.insert(f, i);
                    }
                    while num % f == 0 {
                        num /= f;
                    }
                }
                f += 1;
            }
            if num != 1 {
                if factors.contains_key(&num) {
                    uf.union(*factors.get(&num).unwrap(), i);
                } else {
                    factors.insert(num, i);
                }
            }
        }
        return uf.rank(0) == n;
    }
}
