function maxAreaOfIsland(grid: number[][]): number {
    let map = new Map();
    let max = 0;
    for(let i = 0; i < grid.length; i++) {
        for(let j = 0; j < grid[0].length; j++) {
            if(grid[i][j] === 1 && !map.has(`${i}x${j}`))
                max = Math.max(max, helper(grid, i, j, map));
        }
    }
    return max;
};

function helper(grid, i, j, map) {
    if(i < 0 || i >= grid.length) return 0;
    if(j < 0 || j >= grid[0].length) return 0;
    if(grid[i][j] === 0) return 0;
    if(map.has(`${i}x${j}`)) return 0;
    map.set(`${i}x${j}`, true);
    return 1 + helper(grid, i +1, j, map) + helper(grid, i, j + 1, map) + helper(grid, i - 1, j, map)
        + helper(grid, i, j - 1, map);
    
}