function solveNQueens(n: number): string[][] {
    let grid = Array(n).fill(0).map(() => Array(n).fill('.'))
    let seenCol = new Set()
    let seenDia1 = new Set()
    let seenDia2 = new Set()
    let result = []
    let dfs = (row: number) => {
        if(row >= n) {
            result.push(grid.map(e => e.join("")))
            return
        }
        for(let col = 0; col < n; col++) {
            if(seenCol.has(col) || seenDia1.has(row + col) || seenDia2.has(row - col)) continue
            seenCol.add(col)
            seenDia1.add(row + col)
            seenDia2.add(row - col)
            grid[row][col] = "Q"
            dfs(row + 1)
            seenCol.delete(col)
            seenDia1.delete(row + col)
            seenDia2.delete(row - col)
            grid[row][col] = "."
        }
    }
    dfs(0)
    return result
};