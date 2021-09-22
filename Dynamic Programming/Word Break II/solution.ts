function wordBreak(s: string, wordDict: string[]): string[] {
    let dict = new Set()
    for(let w of wordDict) {
        dict.add(w)
    }
    let dp = Array(s.length)
    
    let dfs = (idx) => {
        if(idx >= s.length) {
            return [""]
        }
        if(dp[idx] !== undefined) return dp[idx]
        let result = []
        let str = ""
        for(let i = idx; i < s.length; i++) {
            str += s[i]
            if(dict.has(str)) {
                let next = dfs(i + 1)
                for(let s of next) {
                    if(s !== "") result.push(str + " " + s)
                    else result.push(str)
                }
            }
        }
        dp[idx] = result
        return result
    }
    
    return dfs(0)
};