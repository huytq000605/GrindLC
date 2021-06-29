function minDominoRotations(tops: number[], bottoms: number[]): number {
    let result = Number.MAX_SAFE_INTEGER
    let res1 = calculate(tops[0], tops, bottoms)
    let res2 = calculate(tops[0], bottoms, tops)
    let res3 = calculate(bottoms[0], tops, bottoms)
    let res4 = calculate(bottoms[0], bottoms, tops)
    result = Math.min(res1, res2, res3, res4)
    if(result === Number.MAX_SAFE_INTEGER) {
        return -1
    } else {
        return result
    }
};

function calculate(target: number, allEqualTarget: number[], swapping: number[]): number {
    let result = 0
    for(let i = 0; i < allEqualTarget.length; i++) {
        if(allEqualTarget[i] === target) {
            continue
        } else {
            if(swapping[i] === target) {
                result++
            } else {
                return Number.MAX_SAFE_INTEGER
            }
        }
    }
    return result
}