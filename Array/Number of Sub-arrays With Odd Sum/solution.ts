function numOfSubarrays(arr: number[]): number {
    let result = 0
    let sum = 0 
    let noOfEvenPrefix = 1 // We have 0 already
    let noOfOddPrefix = 0
    let MOD = 1e9 + 7
    for(let i = 0; i < arr.length; i++) {
        sum += arr[i]
        if(sum % 2 === 0) {
            result += noOfOddPrefix
            result = result % MOD
            noOfEvenPrefix++
        } else {
            result += noOfEvenPrefix
            result = result % MOD
            noOfOddPrefix++
        }
    }
    return result
};