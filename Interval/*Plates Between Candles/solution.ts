function platesBetweenCandles(s: string, queries: number[][]): number[] {
    let leftToRight = Array(s.length)
    let rightToLeft = Array(s.length)
    let prefix = Array(s.length)
    let candles = -1
    let plates = 0
    for(let i = 0; i < s.length; i++) {
        if(s[i] === "|") candles = i
        else plates++
        leftToRight[i] = candles
        prefix[i] = plates
    }
    
    candles = -1
    for(let i = s.length - 1; i >= 0; i--) {
        if(s[i] === "|") candles = i
        rightToLeft[i] = candles
    }
    let result = Array(queries.length).fill(0)
    
    for(let i = 0; i < queries.length; i++) {
        let [left, right] = queries[i]
        let leftCandles = rightToLeft[left]
        let rightCandles = leftToRight[right]
        if(leftCandles === -1 || rightCandles === -1 || leftCandles >= rightCandles) {
            result[i] = 0
        } else {
            if(leftCandles === 0) {
                result[i] = prefix[rightCandles]
            } else {
                result[i] = prefix[rightCandles] - prefix[leftCandles - 1]
            }
        }
    }
    return result
};