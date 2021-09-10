function numberOfArithmeticSlices(nums: number[]): number {
    let result = 0
    let dp = Array(nums.length).fill(0).map(() => Array(nums.length).fill(0).map(() => Array(2)))
    // let map = new Map()
    
    let dfs = (first: number, second: number, starting: number /* 0 or 1 */) => {
        // if(dp[first][second][starting]) return dp[first][second][starting]
        // let key = `${first},${second},${starting}`
        // if(map.has(key)) return map.get(key)
        let result = 0
        if(!starting) result = 1
        for(let next = second + 1; next < nums.length; next++) {
            if(nums[next] - nums[second] === nums[second] - nums[first]) {
                result += dfs(second, next, 0)
            }
        }
        dp[first][second][starting] = result
        // map.set(key, result)
        return result
    }
    
    
    for(let i = 0; i < nums.length - 2; i++) {
        for(let j = i + 1; j < nums.length - 1; j++) {
            result += dfs(i, j, 1)
        }
    }
    return result
    
    
};