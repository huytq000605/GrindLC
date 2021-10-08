// Tricky problem

// To understand this problem
// First, we think about 2 number a and b, a < b, there are 4 cases
// [a,b] => [a-k, b-k], [a-k, b+k], [a+k, b-k], [a+k, b+k]
// [a-k, b-k] and [a+k, b+k] doesn't make any differences
// [a-k, b+k] just make the diff between them more far away
// So we just need to consider [a+k, b-k]

// In this problem, we sort the array. Iterate through the array
// We assume a[i] is the maximum value, then all elements belong to the range [i + 1, n] must - k
// And, all elements belong to the range [0, i] must + k (like the above explanation)
// So if a[i] is not the maximum, the maximum will be a[n] - k
// The minimum will be a[0] + k or a[i + 1] - k
// (Imagine we divide array into 2 subarray)
// [arr[0] + k, arr[1] + k, ... arr[i] + k] || [arr[i + 1] - k, .... arr[n] - k]

function smallestRangeII(nums: number[], k: number): number {
    nums.sort((a,b) => a-b)
    let result = nums[nums.length - 1] - nums[0]
    for(let i = 0; i < nums.length - 1; i++) {
        let min = Math.min(nums[0] + k, nums[i + 1] - k)
        let max = Math.max(nums[i] + k, nums[nums.length - 1] - k)
        result = Math.min(result, max - min)
    }
    return result
};