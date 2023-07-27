impl Solution {
    pub fn max_run_time(n: i32, mut batteries: Vec<i32>) -> i64 {
        // We wants to split the batteries evenly
        // So the best option would be sum(batteries) // n
        // But if there is a very big battery
        // We just plug it in 1 computer forever
        // Then solve the problem with n-1 computers and batteries - battery
        batteries.sort();
        let mut n = n as i64;
        let mut s: i64 = batteries.iter().map(|&e| e as i64).sum();
        while n > 1 && batteries[batteries.len() - 1] as i64 > s / n {
            s -= batteries.pop().unwrap() as i64;
            n -= 1;
        } 
        return s / n
    }
}
