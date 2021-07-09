/*
Idea: Check for all sliding window
*/
function characterReplacement(s: string, k: number): number {
    let alphabet = new Map()
    let start = 0
    let result = 1
    let originalK = k
    for(let i = 0; i < s.length; i++) { 
		alphabet.set(s[i], (alphabet.get(s[i]) || 0) + 1)
        if(s[i] !== s[start]) {
            k--
            while(k < 0) {
                alphabet.set(s[start], alphabet.get(s[start]) - 1)
                start++
                k = originalK
                for(let [letter, freq] of alphabet.entries()) {
                    if(letter !== s[start]) {
                        k -= freq
                    }
                }
            }
        }
        
        result = Math.max(result, Math.min(i - start + 1 + k, s.length)) // If this sliding window still have k, so + k for longer, if over range => we need to compare with maximum length it can have
    }
    return result
};
