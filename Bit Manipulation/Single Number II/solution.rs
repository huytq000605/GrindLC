impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut bit = vec![0; 32];
        for num in nums {
            for i in 0..32 {
                if (num >> i) & 1 == 1 {
                    bit[i] += 1;
                }
            }
        }
        let mut result = 0;
        for i in 0..32 {
            if bit[i] % 3 != 0 {
                result |= (1 << i);
            }
        }
        result
    }
}
