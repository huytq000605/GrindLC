function platesBetweenCandles(s: string, queries: number[][]): number[] {
    let candles = []
    let prefix = Array(s.length)
    let plates = 0
    for(let i = 0; i < s.length; i++) {
        if(s[i] === "|") {
            candles.push(i)
        } else {
            plates++
        }
        
        prefix[i] = plates
        
    } 
    
    let result = Array(queries.length).fill(0)
    for(let i = 0; i < queries.length; i++) {
        let [left, right] = queries[i]
        let min = 0
        let max = candles.length - 1
        while(min < max) {
            let mid = min + Math.floor((max - min) / 2)
            if(candles[mid] >= left) {
                max = mid
            } else {
                min = mid + 1
            }
        }
        let leftCandles = candles[min]
        if(leftCandles < left || leftCandles > right) continue
        
        
        min = 0
        max = candles.length - 1
        while(min < max) {
            let mid = min + Math.ceil((max - min + 1) / 2)
            if(candles[mid] <= right) {
                min = mid
            } else {
                max = mid - 1
            }
        }
        let rightCandles = candles[min]
        if(rightCandles > right || rightCandles < left) continue
        
        if(leftCandles === 0) result[i] = prefix[rightCandles]
        else result[i] = prefix[rightCandles] - prefix[leftCandles - 1]
    
    }
    return result
};