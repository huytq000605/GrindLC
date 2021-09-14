function findSubstringInWraproundString(p: string): number {
    let dp = Array(26).fill(0) // dp[i] = num of subString end with char i
    let currentLength = 0
    for(let i = 0; i < p.length; i++) {
        if(i === 0 || p.charCodeAt(i) === p.charCodeAt(i - 1) + 1 || p[i-1] === "z" && p[i] === "a") {
            currentLength++
        } else {
            currentLength = 1
        }
        dp[p.charCodeAt(i) - "a".charCodeAt(0)] = Math.max(dp[p.charCodeAt(i) - "a".charCodeAt(0)], currentLength)
    }
    
    let result = 0
    for(let i = 0; i < dp.length; i++) {
        result += dp[i]
    }
    return result
};