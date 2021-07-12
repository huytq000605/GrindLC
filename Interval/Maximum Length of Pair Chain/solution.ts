function findLongestChain(pairs: number[][]): number {
    pairs.sort((a,b) => a[1] - b[1])
    let result = 0
    let last = Number.MIN_SAFE_INTEGER
    for(let pair of pairs) {
        if(pair[0] > last) {
            result++
            last = pair[1]
        }
    }
    return result
};
