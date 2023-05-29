struct TicTacToe {
    rs: Vec<i32>,
    cs: Vec<i32>,
    dia: i32,
    anti_dia: i32,
    n: i32
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TicTacToe {

    fn new(n: i32) -> Self {
        return TicTacToe{
            rs: vec![0; n as usize],
            cs: vec![0; n as usize],
            dia: 0,
            anti_dia: 0,
            n: n
        }
    }
    
    fn make_a_move(&mut self, row: i32, col: i32, player: i32) -> i32 {
        let (r, c, p): (i32, i32, i32) = (row, col, player*2-3);
        self.rs[r as usize] += p;
        self.cs[c as usize] += p;
        if r == c { self.dia += p }
        if r + c == self.n - 1 { self.anti_dia += p }
        let values = vec![self.rs[r as usize], self.cs[c as usize], self.dia, self.anti_dia];
        if values.contains(&self.n) {
            2
        } else if values.contains(&(-self.n)) {
            1
        } else {
            0
        }
    }
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * let obj = TicTacToe::new(n);
 * let ret_1: i32 = obj.move(row, col, player);
 */
