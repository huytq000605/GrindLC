function lengthOfLongestSubstring(s: string): number {
    let max = 0;
    let start = 0
    let set = new Set()
    for(let i = 0, j = 0; i < s.length; i++) {
        while(set.has(s[i])) {
            set.delete(s[start])
            start++
        }
        max = Math.max(max, i - start + 1)
    }
	return max;
};