function canJump(nums: number[]): boolean {
    let cache = Array(nums.length)
    let dfs = (index) => {
        if(index === nums.length - 1) {
            return true
        }
        if(index > nums.length) return false
        if(cache[index] !== undefined) return false
        for(let i = 1; i <= nums[index]; i++) {
            if(dfs(index + i)) return true
        }
        cache[index] = false
        return false
    }
    return dfs(0)
    
};