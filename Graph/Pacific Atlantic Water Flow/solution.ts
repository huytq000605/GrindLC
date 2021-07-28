function pacificAtlantic(heights: number[][]): number[][] {
    let pacific = Array(heights.length).fill(0).map(() => Array(heights[0].length))
    let atlantic = Array(heights.length).fill(0).map(() => Array(heights[0].length))
    
    let dirs = [[0,1], [1,0], [-1,0], [0, -1]]
    function dfs(i: number, j: number, unionFind: boolean[][]) {
        if(unionFind[i][j] === true) return
        unionFind[i][j] = true
        for(let dir of dirs) {
            let newRow = i + dir[0]
            let newCol = j + dir[1]
            if(newRow < 0 || newRow >= heights.length || newCol < 0 || newCol >= heights[0].length || unionFind[newRow][newCol] === true || heights[newRow][newCol] < heights[i][j]) continue
            dfs(newRow, newCol, unionFind)
        }
    }
    let result = []
    for(let i = 0; i < heights.length; i++) {
        dfs(i, 0, pacific)
        dfs(i, heights[0].length - 1, atlantic)
    }
    for(let i = 0; i < heights[0].length; i++) {
        dfs(0, i, pacific)
        dfs(heights.length - 1, i, atlantic)
    }
    for(let i = 0; i < heights.length; i++) {
        for(let j = 0; j < heights[0].length; j++) {
            if(pacific[i][j] === true && atlantic[i][j] === true) {
                result.push([i,j])
            }
        }
    }
    return result
};