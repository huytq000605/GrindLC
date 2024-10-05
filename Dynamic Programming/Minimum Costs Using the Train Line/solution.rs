impl Solution {
    pub fn minimum_costs(regular: Vec<i32>, express: Vec<i32>, express_cost: i32) -> Vec<i64> {
        let express_cost = express_cost as i64;
        let (mut reg, mut exp) = (0 as i64, express_cost);
        let mut result = vec![0; regular.len()];
        for i in 0..regular.len() {
            let new_reg = std::cmp::min(reg + regular[i] as i64, exp + regular[i] as i64);
            let new_exp = std::cmp::min(reg + express_cost + express[i] as i64, exp + express[i] as i64);
            result[i] = std::cmp::min(new_reg, new_exp);
            reg = new_reg;
            exp = new_exp;
        }
        return result
    }
}
