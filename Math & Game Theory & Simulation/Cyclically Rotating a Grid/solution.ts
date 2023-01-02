function rotateGrid(grid: number[][], k: number): number[][] {
    let firstRow = 0
    let firstCol = 0
    let lastRow = grid.length - 1
    let lastCol = grid[0].length - 1
    let layers = Array(Math.min(grid.length, grid[0].length) / 2).fill(0).map(() => [])
    let layer = 0
    while(firstRow < lastRow && firstCol < lastCol) {
        // left
        for(let row = firstRow; row <= lastRow; row++) {
            layers[layer].push(grid[row][firstCol])
        }
        // down
        for(let col = firstCol + 1; col <= lastCol; col++) {
            layers[layer].push(grid[lastRow][col])
        }
        // right
        for(let row = lastRow - 1; row >= firstRow; row--) {
            layers[layer].push(grid[row][lastCol])
        }
        //top
        for(let col = lastCol - 1; col > firstCol; col--) {
            layers[layer].push(grid[firstRow][col])
        }
        layer++
        firstRow++
        firstCol++
        lastRow--
        lastCol--
    }
    
    let startingIndexLayer = Array(layers.length)
    for(let i = 0; i < startingIndexLayer.length; i++) {
        startingIndexLayer[i] = layers[i].length - k % layers[i].length
    }
    
    let result = Array(grid.length).fill(0).map(() => Array(grid[0].length))
    
    firstRow = 0
    firstCol = 0
    lastRow = grid.length - 1
    lastCol = grid[0].length - 1
    layer = 0
    while(firstRow < lastRow && firstCol < lastCol) {
        let layerLength = layers[layer].length
        // left
        for(let row = firstRow; row <= lastRow; row++) {
            result[row][firstCol] = layers[layer][(startingIndexLayer[layer]++) % layerLength]
        }
        // down
        for(let col = firstCol + 1; col <= lastCol; col++) {
            result[lastRow][col]= layers[layer][(startingIndexLayer[layer]++) % layerLength]
        }
        // right
        for(let row = lastRow - 1; row >= firstRow; row--) {
            result[row][lastCol] = layers[layer][(startingIndexLayer[layer]++) % layerLength]
        }
        //top
        for(let col = lastCol - 1; col > firstCol; col--) {
            result[firstRow][col] = layers[layer][(startingIndexLayer[layer]++) % layerLength]
        }
        layer++
        firstRow++
        firstCol++
        lastRow--
        lastCol--
    }
    return result
};