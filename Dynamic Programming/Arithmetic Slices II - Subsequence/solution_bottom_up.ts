// dp[i] is a hash map stores number of subsequence (at least 2 elements) that have each element[i+1] - element[i] = diff with diff as a  key
function numberOfArithmeticSlices(nums: number[]): number {
    let dp = Array(nums.length).fill(0).map(() => new Map())
    let result = 0
    for(let i = 0; i < nums.length; i++) {
        for(let j = 0; j < i; j++) {
            let diff = nums[i] - nums[j]
            let count = dp[j].get(diff) || 0
            dp[i].set(diff, (dp[i].get(diff) || 0) + count + 1)
			// Only + count to result because that makes a subsequence have at least 3 elements
            result += count
        }
    }
    return result
};