function countSubIslands(grid1: number[][], grid2: number[][]): number {
    let m = grid1.length;
    let n = grid1[0].length
    
    let result = 0;
    let seen = new Map()
	function dfs(i, j) {
		if(i < 0 || i === m || j < 0 || j === n || grid2[i][j] !== 1) {
			return 0
		}
		if(grid1[i][j] !== 1) {
			return -1 // This island is not in grid1
		}
		let key = `${i}-${j}`
		if(seen.has(key)) {
			return 0
		}
		
		seen.set(key, true)
		
		let res1 = dfs(i - 1, j)
		let res2 = dfs(i + 1, j)
		let res3 = dfs(i, j - 1)
		let res4 = dfs(i, j + 1)
		if(res1 === -1 || res2 === -1 || res3 === -1 || res4 === - 1) { // This island is not in grid1
			return -1 
		}
		
		return 1
		
	}
    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            if(grid2[i][j] === 1 && grid1[i][j] === 1) {
                let res = dfs(i,j)
                if(res > 0) result += res
            }

        }
    }
    
    return result
};
    