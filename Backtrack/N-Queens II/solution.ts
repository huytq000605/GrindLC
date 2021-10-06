function totalNQueens(n: number): number {
    let seenCol = new Set()
    let seenDia1 = new Set()
    let seenDia2 = new Set()
    let result = 0
    let dfs = (row: number) => {
        if(row >= n) {
            result++
            return
        }
        for(let col = 0; col < n; col++) {
            if(seenCol.has(col) || seenDia1.has(row + col) || seenDia2.has(row - col)) continue
            seenCol.add(col)
            seenDia1.add(row + col)
            seenDia2.add(row - col)
            dfs(row + 1)
            seenCol.delete(col)
            seenDia1.delete(row + col)
            seenDia2.delete(row - col)
        }
    }
    dfs(0)
    return result
};