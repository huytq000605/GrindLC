impl Solution {
    pub fn num_of_minutes(n: i32, head_id: i32, managers: Vec<i32>, inform_time: Vec<i32>) -> i32 {
        let mut in_deg = vec![0; n as usize];
        for (report, &manager) in managers.iter().enumerate() {
            if manager == -1 { continue }
            in_deg[manager as usize] += 1
        }
        let mut leafs = std::collections::VecDeque::new();
        for (employee, &reports) in in_deg.iter().enumerate() {
            if employee != head_id as usize && reports == 0 {
                leafs.push_back(employee);
            }
        }
        let mut done_inform = inform_time.clone();
        while leafs.len() > 0 {
            let employee = leafs.pop_front().unwrap();
            if employee == head_id as usize {
                continue
            }
            let manager = managers[employee] as usize;
            done_inform[manager] = std::cmp::max(done_inform[manager], done_inform[employee] + inform_time[manager]);
            leafs.push_back(manager);
        }
        return done_inform[head_id as usize]
    }
}
