impl Solution {
    pub fn is_happy(n: i32) -> bool {
        let (mut slow, mut fast) = (n, n);
        fn sum_square_digit(mut num: i32) -> i32 {
            let mut result = 0;
            while num > 0 {
                result += (num % 10) * (num % 10);
                num /= 10;
            }
            return result
        }
        
        while fast != 1 {
            fast = sum_square_digit((sum_square_digit(fast)));
            slow = sum_square_digit(slow);
            if slow == fast {
                break
            }
        }
        return fast == 1;
    }
}
