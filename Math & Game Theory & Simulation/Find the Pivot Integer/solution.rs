impl Solution {
    pub fn pivot_integer(n: i32) -> i32 {
        // 1+2+3+...+x = x+x+1+x+2+...+n
        // (x+1) * x // 2 = n*(n+1)//2 - (x+1) * x // 2 - x
        // (x+1)*x - x = n*(n+1)//2
        // x**2 = n*(n+1)//2
        let xx = (n*(n+1)) as f64 / 2.0;
        let x = f64::sqrt(xx);
        if f64::round(x) == x {
            return x as i32
        }
        -1
    }
}
