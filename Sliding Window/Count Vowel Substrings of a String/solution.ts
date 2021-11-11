function countVowelSubstrings(word: string): number {
    let atMost = (k) => {
        let result = 0
        let map = new Map()
        let start = 0
        for(let i = 0; i < word.length; i++) {
            if(word[i] === "u" || word[i] === "e" || word[i] === "o" || word[i] === "a" || word[i] === "i") {
                map.set(word[i], (map.get(word[i]) || 0) + 1)
            } else {
                map.clear()
                start = i + 1
                continue
            }
            while(map.size > k) {
                map.set(word[start], map.get(word[start]) - 1)
                if(map.get(word[start]) === 0) map.delete(word[start])
                start++
            }
            result += i - start + 1
        }
        return result
    }
    return atMost(5) - atMost(4)
};