/*
If sum of a sub array (contiguous) have index from [i,j] is % k === 0 => (prefixSum[j] - prefix[i - 1]) % k === 0 => prefixSum[j] % k = prefix[i-1] % k
*/

function subarraysDivByK(nums: number[], k: number): number {
    let map = new Map()
    let result = 0
    map.set(0, 1) // Default value for 0
    let sum = 0
    for(let i = 0; i < nums.length; i++) {
        sum += nums[i]
        let remainder = ( sum % k + k ) % k
        result += map.get(remainder) || 0
        map.set(remainder, (map.get(remainder) || 0 ) + 1)
    }
    return result
};
