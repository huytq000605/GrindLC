impl Solution {
    pub fn get_maximum_consecutive(mut coins: Vec<i32>) -> i32 {
        coins.sort();
        let mut sum = 0;
        for coin in coins {
            if coin > sum + 1 {
                break
            }
            sum += coin;
        }
        return sum + 1
    }
}
