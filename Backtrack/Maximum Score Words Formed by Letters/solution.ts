function maxScoreWords(words: string[], letters: string[], score: number[]): number {
    // Create letter bank
    let letterBank = new Map()
    for(let letter of letters) {
        letterBank.set(letter, (letterBank.get(letter) || 0) + 1)
    }

    function helper(words: string[], letterBank: Map<string, number>) { // DFS
		// Can memoization the map object with JSON.stringify(Array.from(letterBank))
        let result = 0
        nextWord:
        for(let [index, word] of words.entries()) { // Loop for each word
            let copyLetterBank: Map<string, number> = new Map(letterBank) // Map is pass by reference => need to create a new one
            let point = 0
            for(let s of word) {
                if(copyLetterBank.has(s) && copyLetterBank.get(s) > 0) { // If our bank still has enough letter => take from it
                    point += score[s.charCodeAt(0) - 97]
                    copyLetterBank.set(s, copyLetterBank.get(s) - 1);
                } else { // If our bank doesn't have enough letter => go to next word
                    continue nextWord
                }
            }
            // Go dfs then store maximum value
            result = Math.max(result, point + helper(words.slice(0, index).concat(words.slice(index + 1)), copyLetterBank))
        }
        return result
    }

    return helper(words, letterBank)
};