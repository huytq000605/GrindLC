impl Solution {
    pub fn is_bipartite(graph: Vec<Vec<i32>>) -> bool {
        let n = graph.len();
        let mut colors = vec![0; n];
        fn dfs(u: i32, c: i32, colors: &mut Vec<i32>, graph: &Vec<Vec<i32>>) -> i32 {
            if colors[u as usize] != 0 {
                if colors[u as usize] != c {
                    return 0
                }
                return c
            }
            colors[u as usize] = c;
            for v in &graph[u as usize] {
                if dfs(*v, 3-c, colors, graph) == 0 {
                    return 0
                }
            }
            return c
        }
        for u in 0..n {
            if colors[u] == 0 {
                if dfs(u as i32, 1, &mut colors, &graph) == 0 {
                    return false
                }
            }
        }
        return true
    }
}
