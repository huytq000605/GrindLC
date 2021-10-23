function findAllConcatenatedWordsInADict(words: string[]): string[] {
    let dict = new Set(words)
    let cache = new Map()
    let canForm = (word) => {
        if(cache.has(word)) return cache.get(word)
        for(let i = 1; i < word.length; i++) {
            if(dict.has(word.slice(0, i))) {
                let suffix = word.slice(i)
                if(dict.has(suffix) || canForm(suffix)) {
                    cache.set(word, true)
                    return true
                }
            }
        }
        cache.set(word, false) 
        return false
        
    }
    let result = []
    for(let word of words) {
        if(canForm(word)) result.push(word)
    }
    return result
};