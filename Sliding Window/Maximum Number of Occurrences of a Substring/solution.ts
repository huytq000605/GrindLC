function maxFreq(s: string, maxLetters: number, minSize: number, maxSize: number): number {
    let result = 0
    for(let size = minSize; size <= maxSize; size++) { // Actually, in this problem, we can just so the size = minSize !!!
        let freq = new Map() // Frequency for letters frequency in sliding window
        let stringMap = new Map() // Frequency for valid sliding window

		// Set the initial sliding window ( starting from 0, ending at size - 1)
        for(let i = 0; i < size; i++) {
            freq.set(s[i], (freq.get(s[i]) || 0) + 1)
        }
        if(freq.size <= maxLetters) {
            let currentString = s.slice(0, size)
            stringMap.set(currentString, (stringMap.get(currentString) || 0) + 1)
        }

		// Finding all valid sliding window
        let start = 1
        for(let end = size; end < s.length; end++) {
            let previousLetterFreq = freq.get(s[start-1])
            if(previousLetterFreq === 1) {
                freq.delete(s[start-1])
            } else {
                freq.set(s[start-1], previousLetterFreq - 1)
            }
            freq.set(s[end], (freq.get(s[end]) || 0)  + 1)
            if(freq.size <= maxLetters) {
                let currentString = s.slice(start, end + 1)
                stringMap.set(currentString, (stringMap.get(currentString) || 0) + 1)
            }
            start++
        }

		// Maximum freq sliding window and update result
        let maximumForThisSize = Math.max(...stringMap.values())
        result = Math.max(result, maximumForThisSize)
    }
    return result
};