function numDecodings(s: string): number {
    let cache = new Map()
    function helper(s: string, index: number) {
        if(index >= s.length) {
            return 1
        }
        if(cache.has(index)) {
            return cache.get(index)
        }
        let decodeThis = 0
        let decodeTwo = 0
        if(index < s.length && s[index] === "0") {
            return 0
        }
        if(index + 1 <= s.length && s[index + 1] === "0") {
            if(s[index] === "*") {
                decodeThis = 2 * helper(s, index + 2)
            } else if(s[index] === "1" || s[index] === "2") {
                decodeThis = helper(s, index + 2)
            }
        } else if(s[index] === "*") {
            decodeThis = 9 * helper(s, index + 1)
        } else {
            decodeThis = helper(s, index + 1)
        }
        
        if(index + 1 <= s.length - 1 && s[index] !== "0" && s[index + 1] !== "0") {
            if(s[index] === "*") {
                if(s[index + 1] === "*") decodeTwo = 15 * helper(s, index + 2)
                else if(Number(s[index + 1]) <= 6) decodeTwo = 2 * helper(s, index + 2)
                else if(Number(s[index + 1]) > 6) decodeTwo = helper(s, index + 2)
            } else if(s[index] === "1") {
                if(s[index + 1] === "*") decodeTwo = 9 * helper(s, index + 2)
                else decodeTwo = helper(s, index + 2)
            } else if(s[index] === "2") {
                if(s[index + 1] === "*") decodeTwo = 6 * helper(s, index + 2)
                else if(Number(s[index + 1]) <= 6) decodeTwo = helper(s, index + 2)
            }
        }
        cache.set(index, (decodeThis + decodeTwo) % 1000000007)
        return cache.get(index)
    }
    
    let result = helper(s, 0)
    return result 
    
};

