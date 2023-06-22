impl Solution {
    pub fn max_profit(prices: Vec<i32>, fee: i32) -> i32 {
        let n = prices.len();
        let (mut empty, mut hold) = (0, -prices[0]);
        let mut result = 0;
        for i in 1..n {
            let new_empty = std::cmp::max(empty, hold + prices[i] - fee);
            let new_hold = std::cmp::max(hold, empty - prices[i]);
            empty = new_empty;
            hold = new_hold;
        }
        return empty
    }
}
