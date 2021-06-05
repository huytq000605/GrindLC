function minDeletions(s: string): number {
    let freq = new Map()
    for(let i = 0; i < s.length; i++) {
        freq.set(s[i], (freq.get(s[i]) || 0) + 1)
    }
    let freqUsed = new Map()
    let result = 0
    for(let value of freq.values()) {
        while(freqUsed.has(value)) {
            value--
            result++
        }
        if(value != 0) {
            freqUsed.set(value, true)
        }
    }
    return result
};