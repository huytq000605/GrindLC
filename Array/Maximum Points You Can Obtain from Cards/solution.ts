function maxScore(cardPoints: number[], k: number): number {
    let prefixSum = Array(cardPoints.length).fill(0)
    for(let i = 0; i < cardPoints.length; i++) {
        if(i === 0) prefixSum[i] = cardPoints[i]
        else prefixSum[i] = prefixSum[i - 1] + cardPoints[i]
    }
    let minSubArray = Number.MAX_SAFE_INTEGER
    k = cardPoints.length - k // Find subarray length k that has minimum sum
    if(k === 0) return prefixSum[prefixSum.length -1]
    for(let i = k - 1; i < cardPoints.length; i++) {
        if(i === k - 1) minSubArray = Math.min(minSubArray, prefixSum[i])
        else minSubArray = Math.min(minSubArray, prefixSum[i] - prefixSum[i - k])
    }
    return prefixSum[cardPoints.length - 1] - minSubArray
};

