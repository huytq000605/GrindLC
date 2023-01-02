function stoneGame(piles: number[]): boolean {
    let cache = new Array(piles.length).fill(0).map(() => Array(piles.length).fill(0).map(() => Array(2)))
    let calculate = (start: number , end: number, alexTurn: number) => {
        if(start > end) {
            return 0
        }
        if(cache[start][end][alexTurn] !== undefined) return cache[start][end][alexTurn]
        if(alexTurn) {
            let getLeft = piles[start] + calculate(start + 1, end, 0)
            let getRight = piles[end] + calculate(start, end - 1, 0)
            cache[start][end][alexTurn] = Math.max(getLeft, getRight)
        } else {
            let getLeft = -piles[start] + calculate(start + 1, end , 1)
            let getRight = -piles[end] + calculate(start, end -1, 1)
            cache[start][end][alexTurn] = Math.min(getLeft, getRight)
        }
        return cache[start][end][alexTurn]
    }
    let point = calculate(0, piles.length - 1, 1)
    if(point < 0) return false
    else return true
};