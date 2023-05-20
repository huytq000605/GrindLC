use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn calc_equation(equations: Vec<Vec<String>>, values: Vec<f64>, queries: Vec<Vec<String>>) -> Vec<f64> {
        let mut graph = HashMap::new();
        for (i, eq) in equations.iter().enumerate() {
            let a = &eq[0];
            let b = &eq[1];
            let v = values[i];
            if !graph.contains_key(b) {
                graph.insert(b.to_string(), HashMap::new());
            }
            let mut in_map = graph.get_mut(b).unwrap();
            in_map.insert(a.to_string(), v);
            if !graph.contains_key(a) {
                graph.insert(a.to_string(), HashMap::new());
            }
            in_map = graph.get_mut(a).unwrap();
            in_map.insert(b.to_string(), 1.0/v);
        }
        fn dfs(graph: & HashMap<String, HashMap<String, f64>>, a: String, b: String, seen: &mut HashSet<String>) -> f64 {
            if a == b {
                return 1.0
            }
            for (c, v) in graph.get(&b).unwrap().iter() {
                if seen.contains(c) {
                    continue
                }
                seen.insert(c.to_string());
                let a_div_c = dfs(graph, a.clone(), c.to_string(), seen);
                if a_div_c != -1.0 {
                    return a_div_c * v
                }
            }
            return -1.0
        }

        let mut result = vec![];
        let mut hash_set = HashSet::new();

        for query in queries.iter() {
            let (a, b) = (&query[0], &query[1]);
            if !graph.contains_key(a) || !graph.contains_key(b) {
                result.push(-1.0);
                continue
            }
            hash_set.insert(b.to_string());
            result.push(dfs(&mut graph, a.to_string(), b.to_string(), &mut hash_set));
            hash_set.clear();
        }
        return result;
    }
}
