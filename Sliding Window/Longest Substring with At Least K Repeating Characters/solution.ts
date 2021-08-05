/*
The key point is that we only have 26 letter 
=> We choose the number of unique letter in sliding window from 1 to 26
*/

function longestSubstring(s: string, k: number): number {
    let result = Array(27).fill(0)
    let check = (freq) => {
        for(let num of freq) {
            if(num > 0 && num < k) return false
        }
        return true
    }
    for(let unique = 1; unique <= 26; unique++) {
        let freq = Array(26).fill(0)
        let start = 0
        let currentUnique = 0
        for(let end = 0; end < s.length; end++) {
            freq[s.charCodeAt(end) - "a".charCodeAt(0)]++
            if(freq[s.charCodeAt(end) - "a".charCodeAt(0)] === 1) {
                currentUnique++
                while(currentUnique > unique) {
                    freq[s.charCodeAt(start) - "a".charCodeAt(0)]--
                    if(freq[s.charCodeAt(start) - "a".charCodeAt(0)] === 0) {
                        currentUnique--
                    }
                    start++
                }
            }
            if(check(freq)) {
                result[unique] = Math.max(result[unique], end - start + 1)
            }
            
        }
        
    }
    return Math.max(...result)
};