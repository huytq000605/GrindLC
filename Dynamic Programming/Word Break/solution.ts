function wordBreak(s: string, wordDict: string[]): boolean {
    let word = new Set()
    for(let w of wordDict) {
        word.add(w)
    }
    let cache = new Array(s.length)
    let helper = (i) => {
        if(i >= s.length) return true
        if(cache[i] !== undefined) return cache[i]
        let current = ""
        for(let j = i; j < s.length; j++) {
            current += s[j]
            if(word.has(current)) {
                if(helper(j + 1) === true) return true
            }
        }
        cache[i] = false
        return false
    }
    return helper(0)
};