impl Solution {
    pub fn maximal_network_rank(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut degree = vec![0; n];
        let mut connected = vec![vec![0; n]; n];
        for road in roads.iter() {
            if let [u, v] = road[..] {
                let (u, v) = (u as usize, v as usize);
                degree[u] += 1;
                degree[v] += 1;
                connected[u][v] = 1;
                connected[v][u] = 1;
            }
        }
        let mut result = 0;
        for u in 0..n {
            for v in u+1..n {
                let res = degree[u] + degree[v] - connected[u][v];
                result = std::cmp::max(result, res as i32);
            }
        }
        return result
    }
}
