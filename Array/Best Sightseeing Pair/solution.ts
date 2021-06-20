function maxScoreSightseeingPair(values: number[]): number {
    let maxValue = values[0];
    let idxMaxValue = 0
    let result = 0
    for(let i = 1; i < values.length; i++) {
        result = Math.max(result, values[i] + maxValue + idxMaxValue - i)
        if(values[i] - maxValue + i - idxMaxValue > 0) {
            maxValue = values[i]
            idxMaxValue = i
        }
    }
    return result
    
    
};