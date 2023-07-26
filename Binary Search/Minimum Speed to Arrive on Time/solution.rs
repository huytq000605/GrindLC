impl Solution {
    pub fn min_speed_on_time(dist: Vec<i32>, hour: f64) -> i32 {
        if hour <= dist.len() as f64 - 1.0 {
            return -1
        }

        fn valid(ds: &Vec<i32>, hour: f64, speed: i32) -> bool {
            let mut time = 0 as f64;
            for &d in ds {
                if time + (d as f64) / (speed as f64) > hour {
                    return false
                }
                time += (d as f64 / speed as f64).ceil();
            }
            return true
        }

        let (mut start, mut end) = (1, 10_000_000);
        while start < end {
            let mid = start + (end - start) / 2;
            if valid(&dist, hour, mid) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start
    }
}
