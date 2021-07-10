function nearestExit(maze: string[][], entrance: number[]): number {
    let queue = [[entrance[0], entrance[1], 0]]
    const dirs = [[0,1], [1,0], [-1, 0], [0, -1]]
    while(queue.length > 0) {
        let [i, j, steps] = queue.shift()
        if(i !== entrance[0] || j !== entrance[1]) {
            if(i === 0 || i === maze.length - 1 || j === 0 || j === maze[0].length - 1) return steps
        }
        if(maze[i][j] === "+") continue
        maze[i][j] = "+"
        for(let dir of dirs) {
            let x = i + dir[0]
            let y = j + dir[1]
            if(x < 0 || x === maze.length || y < 0 || y === maze[0].length || maze[x][y] === "+") continue
            queue.push([x,y,steps + 1])
        }
    }
    return -1
    
};
