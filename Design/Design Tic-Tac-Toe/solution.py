class TicTacToe:

    def __init__(self, n: int):
        self.rs = [0 for _ in range(n)]
        self.cs = [0 for _ in range(n)]
        self.dia = 0
        self.anti_dia = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        if player == 2:
            player = -1
        self.rs[row] += player
        self.cs[col] += player
        if row == col: self.dia += player
        if row + col == self.n-1: self.anti_dia += player
        if self.n in map(abs, [self.rs[row], self.cs[col], self.dia, self.anti_dia]):
            if player == -1: return 2
            return 1
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
