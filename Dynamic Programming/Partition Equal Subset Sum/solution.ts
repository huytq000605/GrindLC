function canPartition(nums: number[]): boolean {
    let sum = 0
    for(let num of nums) {
        sum += num
    }
    if(sum % 2 !== 0) return false
    let target = sum / 2
    let dp = Array(nums.length).fill(0).map(() => Array(target))
    
    let dfs = (index, current) => {
        if(current === target) {
            return true
        }
        if(current > target || index >= nums.length) {
            return false
        }
        if(dp[index][current] !== undefined) return false
        if(dfs(index + 1, current + nums[index]) || dfs(index + 1, current)) return true
        dp[index][current] = false
        return false
    }
    
    return dfs(0, 0)
};

