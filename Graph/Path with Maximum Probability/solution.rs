use std::collections::BinaryHeap;

#[derive(PartialEq, PartialOrd)]
struct NonNanF64(f64);
impl Eq for NonNanF64 {}
impl Ord for NonNanF64 {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.0.partial_cmp(&other.0).unwrap()
    }
}

impl Solution {
    pub fn max_probability(n: i32, edges: Vec<Vec<i32>>, succ_prob: Vec<f64>, start: i32, end: i32) -> f64 {
        let mut pq = BinaryHeap::new();
        pq.push((NonNanF64(1.0), start));
        let mut graph = vec![vec![]; n as usize];
        for i in 0..edges.len() {
            let (u, v) = match &edges[i][..] {
                [u, v] => (*u, *v),
                _ => panic!("err"),
            };
            let p = succ_prob[i];
            graph[u as usize].push((v, p));
            graph[v as usize].push((u, p));
        }

        let mut ps = vec![0.0; n as usize];
        ps[start as usize] = 1.0;
        while pq.len() > 0 {
            let (prob, u) = pq.pop().unwrap();
            for edge in &graph[u as usize] {
                let (v, p) = match edge {
                    (v, p) => (*v, p),
                    _ => panic!("err"),
                };
                if prob.0 * p > ps[v as usize] {
                    ps[v as usize] = prob.0 * p;
                    pq.push((NonNanF64(prob.0 * p), v));
                }
            }
        }
        return ps[end as usize]
    }
}
