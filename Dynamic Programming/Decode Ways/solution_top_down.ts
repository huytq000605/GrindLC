function numDecodings(s: string): number {
    let cache = Array(s.length)
    let helper = (index: number) => {
        if(index === s.length) return 1
        if(cache[index] !== undefined) return cache[index]
        if(s[index] === "0") {
            cache[index] = 0
            return cache[index]
        }
        let result = 0
        if(index < s.length - 1 && (s[index] === "1" || (s[index] === "2" && s[index + 1] < "7" ))) {
            result += helper(index + 2)
        }
        result += helper(index + 1)
        cache[index] = result
        return result
    }
    return helper(0)
};