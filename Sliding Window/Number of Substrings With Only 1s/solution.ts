function numSub(s: string): number {
    let result = 0
    let count = 0
    for(let i = 0; i < s.length; i++) {
        if(s[i] === "1") count++
        else if(count > 0) {
            result += ((count) * (count + 1) / 2) % (1e9 + 7)
            result = result % (1e9 + 7)
            count = 0
        }
    }
    result += ((count) * (count + 1) / 2) % (1e9 + 7)
    result = result % (1e9 + 7)
    return result
};