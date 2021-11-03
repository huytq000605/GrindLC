function isScramble(s1: string, s2: string): boolean {
    let cache = new Map()
    let dfs = (s1: string, s2: string) => {
        if(s1 === s2) return true
        const key = s1 + "," + s2
        if(cache.has(key)) return cache.get(key)
        for(let i = 0; i < s1.length - 1; i++) {
            let left1 = s1.slice(0, i + 1)
            let right1 = s1.slice(i + 1)
            let left2 = s2.slice(0, i + 1)
            let right2 = s2.slice(i + 1)
            let swapLeft2 = s2.slice(0, right1.length)
            let swapRight2 = s2.slice(right1.length)
            if(dfs(left1, left2) && dfs(right1, right2) ) {
                cache.set(key, true)
                return true
            }
            if(dfs(left1, swapRight2) && dfs(right1, swapLeft2)) {
                cache.set(key, true)
                return true
            }
            
        }
        cache.set(key, false)
        return false
    }
    
    return dfs(s1, s2)
    
};