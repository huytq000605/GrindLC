function numDecodings(s: string): number {
    if(!s.length) return 0
    let dp = Array(s.length + 1).fill(0)
    dp[s.length] = 1
    
    for(let i = s.length -1; i >= 0; i--) {
        if(s[i] === "0") {
            dp[i] = 0
            continue
        }
        if(i < s.length - 1 && (s[i] === "1" || s[i] === "2" && s[i+1] < "7" )) {
            dp[i] += dp[i + 2]
        }
        dp[i] += dp[i+1]
    }
    return dp[0]
    
};