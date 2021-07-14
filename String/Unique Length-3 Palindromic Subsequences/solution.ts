function countPalindromicSubsequence(s: string): number {
    let result = 0
    let first = new Map()
    let last = new Map()
    for(let i = 0; i < s.length; i++) {
        if(!first.has(s[i])) first.set(s[i], i)
        last.set(s[i], i)
    }
    for(let letter of first.keys()) {
        let set = new Set()
        for(let i = first.get(letter) + 1; i < last.get(letter); i++) {
            set.add(s[i])
        }
        result += set.size
    }
    return result
};