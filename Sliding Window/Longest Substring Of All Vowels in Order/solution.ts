function longestBeautifulSubstring(word: string): number {
    let start = 0
    let result = 0
    let set = new Set()
    set.add(word[start])
    for(let end = 1; end < word.length; end++) {
        if(word[end] < word[end - 1]) {
            set = new Set()
            start = end
        }
        set.add(word[end])
        if(set.size === 5) {
            result = Math.max(result, end - start + 1)
        }
    }
    return result
}