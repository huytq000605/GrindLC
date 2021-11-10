function canPartitionKSubsets(nums: number[], k: number): boolean {
    let sum = 0
    for(let num of nums) {
        sum += num
    }
    if(sum % k !== 0) return false
    let target = sum / k
    let states = Array(k).fill(0)

    nums.sort((a,b) => b-a)

    let dfs = (idx: number) => {
        if(idx >= nums.length) return true
        let seen = new Set()
        for(let i = 0; i < states.length; i++) {
            if(seen.has(states[i])) continue
            if(states[i] + nums[idx] <= target) {
                seen.add(states[i])
                states[i] += nums[idx]
                if(dfs(idx + 1)) return true
                states[i] -= nums[idx]
            }
        }
        return false
    }
    return dfs(0)
    
};