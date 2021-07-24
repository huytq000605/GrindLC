function findAnagrams(s: string, p: string): number[] {
    let result = []
    let cmp = Array(26).fill(0)
    let alphabet = Array(26).fill(0)
    for(let i = 0; i < p.length; i++) {
        cmp[s.charCodeAt(i) - 'a'.charCodeAt(0)]++
        alphabet[p.charCodeAt(i) - 'a'.charCodeAt(0)]++
    }
    let start = 0
    if(compare(cmp, alphabet)) result.push(start)
    start++
    for(let end = p.length; end < s.length; end++, start++) {
        cmp[s.charCodeAt(start - 1) - 'a'.charCodeAt(0)]--
        cmp[s.charCodeAt(end) - 'a'.charCodeAt(0)]++
        if(compare(cmp,alphabet)) result.push(start)
    }
    return result
};
    
function compare(cmp: number[], alphabet: number[]): boolean {
    for(let i = 0; i <= 25; i++) {
        if(cmp[i] !== alphabet[i]) return false
    }
    return true
}