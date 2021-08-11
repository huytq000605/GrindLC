function powerfulIntegers(x: number, y: number, bound: number): number[] {
    let set = new Set()
    let dp = Array(100).fill(0).map(() => Array(100))
    let helper = (i, j, currentX, currentY) => {
        if(dp[i][j] !== undefined) return
        if(currentX + currentY > bound) return
        set.add(currentX + currentY)
        dp[i][j] = true
        if(x !== 1) {
            helper(i+1, j, currentX * x, currentY) 
        }
        if(y !== 1) {
            helper(i, j + 1, currentX, currentY * y)
        }
        
    }
    
    helper(0, 0, 1, 1)
    
    return Array.from(set) as number[]
};