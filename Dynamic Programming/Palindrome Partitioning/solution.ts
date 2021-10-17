function partition(s: string): string[][] {
    let dp = Array(s.length)
    let cacheCheck = Array(s.length).fill(0).map(() => Array(s.length))
        
    let isPalindrome = (start, end) => {
        if(cacheCheck[start][end] !== undefined) return cacheCheck[start][end]
        while(start < end) {
            if(s[start] !== s[end]) {
                cacheCheck[start][end] = false
                return false
            }
            start++
            end--
        }
        cacheCheck[start][end] = true
        return true
    }
    
    let dfs = (idx) => {
        if(idx >= s.length) {
            return [""]
        }
        let result = []
        for(let i = idx; i < s.length; i++) {
            if(isPalindrome(idx, i)) {
                let parts = dfs(i + 1)
                for(let part of parts) {
                    result.push([s.slice(idx, i + 1), ...part])
                }
            }
        }
        dp[idx] = result
        return result
    }
    return dfs(0)
};

