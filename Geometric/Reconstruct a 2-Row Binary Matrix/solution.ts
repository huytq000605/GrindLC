function reconstructMatrix(upper: number, lower: number, colsum: number[]): number[][] {
    let result = Array(2).fill(0).map(() => Array(colsum.length))
    for(let col = 0; col < colsum.length; col++) {
        if(colsum[col] === 0) {
            result[0][col] = 0
            result[1][col] = 0
        } else if(colsum[col] === 1) {
            if(upper > 0 && upper >= lower) {
                result[0][col] = 1
                result[1][col] = 0
                upper--
            } else if(lower > 0) {
                result[0][col] = 0
                result[1][col] = 1
                lower--
            } else {
                return []
            }
        } else if(colsum[col] === 2) {
            if(upper > 0 && lower > 0) {
                upper--
                lower--
                result[0][col] = 1
                result[1][col] = 1
            } else {
                return []
            }
        }
    }
    if(upper > 0 || lower > 0) return []
    return result
};