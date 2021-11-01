# @param {Character[][]} board
# @return {Void} Do not return anything, modify board in-place instead.
def solve(board)
    @board = board
    @dirs = [[0,1], [1,0], [0, -1], [-1, 0]]
    def dfs(row, col)
        @board[row][col] = "."
        @dirs.each do |dir|
            newRow = row + dir[0]
            newCol = col + dir[1]
            if newRow < 0 || newRow >= @board.length || newCol < 0 || newCol >= @board[0].length || @board[newRow][newCol] != "O"
                next
            end
            dfs(newRow, newCol)
        end
    end
    
    (0...board[0].length).each do |col|
        if board[0][col] == "O"
            dfs(0, col)
        end
        
        if board.length - 1 != 0 && board[board.length - 1][col] == "O"
            dfs(board.length - 1, col)
        end
    end
    
    (0...board.length).each do |row|
        if board[row][0] == "O"
            dfs(row, 0)
        end
        
        if board[0].length - 1 != 0 && board[row][board[0].length - 1] == "O"
            dfs(row, board[0].length - 1)
        end
    end
    
    board.each do |row|
        (0...row.length).each do |col|
            if row[col] == "."
                row[col] = "O"
            else
                row[col] = "X"
            end
        end
    end
end