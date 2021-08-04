function minSwaps(grid: number[][]): number {
    let n = grid.length
    let rows = Array(n).fill(0)
    for(let row = 0; row < n; row++) { // Count number zero from right to left until meet 1 or out of range for each row
        for(let col = n - 1; col >= 0; col--) {
            if(grid[row][col] === 0) {
                rows[row]++
            } else {
                break
            }
        }
    }
    let result = 0
    for(let r = 0; r < n; r++) {
        let zeroesNeeded = n - r - 1
        if(rows[r] >= zeroesNeeded) continue // This row is satisfy
        let found = -1 // Flag to mark the index
        for(let i=r+1; i < n; i++) { // Find satisfy row from down below, swap it to r if found
            if(rows[i] >= zeroesNeeded) {
                found = i
                break
            }
        }
        if(found === -1) return -1 // If cannot find any satisfy row, then we cant arrange to the result
        for(let i = found; i > r; i--) { // Swap found to r
            [rows[i], rows[i - 1]] = [rows[i - 1], rows[i]]
            result++
        }
        
    }
    return result  
};
