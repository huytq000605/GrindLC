function minWindow(s: string, t: string): string {
    let freq = new Map()
    let result = [-1, - 1]
    for(let letter of t) {
        freq.set(letter, (freq.get(letter) || 0) + 1)
    }
    let start = 0
    for(let end = 0; end < s.length; end++) {
        if(freq.has(s[end])) {
            freq.set(s[end], freq.get(s[end]) - 1)
        }
        while(check(freq)) {
            if(result[0] === -1 && result[1] === -1 || end - start + 1 < result[1] - result[0] + 1) {
                result = [start, end]
            }
            if(freq.has(s[start])) {
                freq.set(s[start], freq.get(s[start]) + 1)
            }
            start++
        }
    }
    if(result[0] === -1) return ""
    return s.slice(result[0], result[1] + 1)
};

function check(freq) {
    for(let value of freq.values()) {
        if(value > 0) {
            return false
        }
    }
    return true
}