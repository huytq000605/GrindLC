function wordSubsets(words1: string[], words2: string[]): string[] {
    let finalFreq = new Map()
    for(let word of words2) {
        let freq = new Map()
        for(let i = 0; i < word.length; i++) {
            freq.set(word[i], (freq.get(word[i]) || 0 ) + 1)
        }
        for(let [key,value] of freq.entries()) {
            if(!finalFreq.has(key)) {
                finalFreq.set(key, value)
            } else {
                finalFreq.set(key, Math.max(finalFreq.get(key), freq.get(key)))
            }
        }
    }
    
    let result = []
    for(let word of words1) {
        let cloneMap = new Map(finalFreq)
        for(let i = 0; i < word.length; i++) {
            if(cloneMap.has(word[i])) {
                let value = cloneMap.get(word[i])
                if(value === 1) {
                    cloneMap.delete(word[i])
                } else {
                    cloneMap.set(word[i], value - 1)
                }
            }
        }
        if(cloneMap.size === 0) {
            result.push(word)
        }
        
    }
    return result
    
};