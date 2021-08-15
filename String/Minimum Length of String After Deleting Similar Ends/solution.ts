function minimumLength(s: string): number {
    let helper = (start, end) => {
        if(start > end) return 0
        if(start === end) return 1
        if(s[start] !== s[end]) return end - start + 1
        while(s[start + 1] === s[start]) {
            start++
        }
        while(s[end - 1] === s[end]) {
            end--
        }
        if(start > end) return 0
        return helper(start + 1, end - 1)  
    }
    return helper(0, s.length - 1)
};