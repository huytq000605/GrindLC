function leastBricks(wall: number[][]): number {
    let numOfBlankInColumn = new Map()
    let maxBlackInColumn = 0
    
    for(let row = 0; row < wall.length; row++) {
        let col = 0;
        for(let i = 0; i < wall[row].length; i++) {
            if(i !== 0) { // No brick yet
                numOfBlankInColumn.set(col, ( numOfBlankInColumn.get(col) || 0 )+ 1 ) // Between each brick is blank
                maxBlackInColumn = Math.max(maxBlackInColumn, numOfBlankInColumn.get(col))
            } 
            col += wall[row][i] // + next Brick width
        }
    }
    
    return wall.length - maxBlackInColumn // No brick in column - Max
};