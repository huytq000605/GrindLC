function numWays(s: string): number {
    let ones = 0
    let MOD = 1e9 + 7
    for(let l of s) {
        if(l === "1") ones++
    }
    if(ones === 0) {
        let result = 0
        for(let i = 0; i < s.length - 1; i++) {
            result += s.length - (i+1) - 1
            result = result % MOD
        }
        return result
    }
    if(ones % 3 !== 0) return 0
    let each = ones / 3
    let current = 0
    let firstInterval = [0, 0]
    let secondInterval = [0, 0]
    for(let i = 0; i < s.length; i++) {
        if(s[i] === "1") {
            current++
            if(current === each) {
                firstInterval[0] = i
            }
            if(current === each + 1) {
                firstInterval[1] = i - 1
            }
            if(current === each * 2) {
                secondInterval[0] = i
            }
            if(current === each * 2 + 1) {
                secondInterval[1] = i - 1
            }
        }
    }
    let first = firstInterval[1] - firstInterval[0] + 1
    let second = secondInterval[1] - secondInterval[0] + 1
    return first * second % MOD
    
};