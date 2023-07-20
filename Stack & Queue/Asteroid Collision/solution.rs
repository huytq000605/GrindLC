impl Solution {
    pub fn asteroid_collision(asteroids: Vec<i32>) -> Vec<i32> {
        let mut result = vec![];
        for a in asteroids {
            let mut explode = false;
            while a < 0 && result.len() > 0 && result[result.len() - 1] > 0 {
                let last = result[result.len() - 1];
                if last < -a {
                    result.pop();
                } else if last == -a {
                    explode = true;
                    result.pop();
                    break
                } else {
                    explode = true;
                    break
                }
            }
            if !explode {
                result.push(a);
            }
        }
        result
    }
}
