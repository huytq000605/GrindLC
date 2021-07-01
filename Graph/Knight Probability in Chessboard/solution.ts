function knightProbability(n: number, k: number, row: number, column: number): number {
    let cache = Array(n).fill(0).map(each => Array(n).fill(0).map(each2 => Array(k)))
    return helper(n, k, row, column, cache)
};

function helper(n: number, k: number, r: number, c: number, cache: number[][][]) {
    if(r < 0 || r >= n || c < 0 || c >= n) {
        return 0
    }
    if(k === 0) {
        return 1
    }
    if(cache[r][c][k] !== undefined) {
        return cache[r][c][k]
    }
    let result = 0;
    const directions = [[1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]
    for(let direction of directions) {
        result += 0.125 * helper(n, k - 1, r + direction[0], c + direction[1], cache)
    }
    cache[r][c][k] = result
    return result
}