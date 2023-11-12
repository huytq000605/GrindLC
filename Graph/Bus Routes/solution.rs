impl Solution {
    pub fn num_buses_to_destination(mut routes: Vec<Vec<i32>>, source: i32, target: i32) -> i32 {
        use std::collections::{HashMap, VecDeque};
        let mut buses = HashMap::<i32, Vec<i32>>::new();
        for (i, route) in routes.iter().enumerate() {
            for &bus in route {
                let mut routes = buses.entry(bus).or_insert(vec![]);
                routes.push(i as i32);
            }
        }

        let mut dq = VecDeque::new();
        dq.push_back((source, 0));

        while dq.len() > 0 {
            let (u, s) = dq.pop_front().unwrap();
            if u == target {
                return s
            }
            for route in buses[&u].iter() {
                for v in routes[*route as usize].iter() {
                    dq.push_back((*v, s+1));
                }
                routes[*route as usize] = vec![];
            }
            buses.insert(u, vec![]);
        }

        return -1
    }
}
