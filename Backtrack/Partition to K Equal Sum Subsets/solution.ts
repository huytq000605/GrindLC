function canPartitionKSubsets(nums: number[], k: number): boolean {
    let sum = 0
    for(let num of nums) sum += num
    if(sum % k !== 0) return false
    let target = sum / k
    let seen = new Set()
    let dfs = (idx: number, group: number, current: number) => {
        if(group === 0) {
            if(seen.size === nums.length) return true
            return false
        }
        if(current === target) {
            return dfs(0, group - 1, 0)
        }
        for(let i = idx; i < nums.length; i++) {
            if(seen.has(i)) continue
            if(current + nums[i] > target) continue
            seen.add(i)
            if(dfs(i + 1, group, current + nums[i])) return true
            seen.delete(i)
        }
        return false
    }
    return dfs(0, k, 0)
};