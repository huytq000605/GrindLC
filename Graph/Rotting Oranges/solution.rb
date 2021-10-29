# @param {Integer[][]} grid
# @return {Integer}
def oranges_rotting(grid)
    deque = []
    deque1 = []
    dirs = [[0,1], [1,0], [-1,0], [0, -1]]
    result = 0
    fresh = 0
    
    (0...grid.length).each do |row|
        (0...grid[0].length).each do |col|
            if grid[row][col] == 1
                fresh += 1
            elsif grid[row][col] == 2
                deque.push([row, col])
            end    
        end
    end
    
    while deque.length > 0
        i, j = deque.shift
        dirs.each do |dir|
            newRow = i + dir[0]
            newCol = j + dir[1]
            if newRow < 0 || newCol < 0 || newRow >= grid.length || newCol >= grid[0].length || grid[newRow][newCol] != 1
                next
            end
            fresh -= 1
            grid[newRow][newCol] = 2
            deque1.push([newRow, newCol])
        end
        if deque.length == 0
            if deque1.length == 0
                break
            end
            result += 1
            deque, deque1 = deque1, deque
        end
        
    end
    
    if fresh != 0
        return -1
    end
    
    result
    
end