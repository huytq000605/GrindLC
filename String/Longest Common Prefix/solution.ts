function longestCommonPrefix(strs: string[]): string {
    let shortest = strs[0]
    for(let i = 1; i < strs.length; i++) {
        if(strs[i].length < shortest.length) {
            shortest = strs[i]
        }
    }
    
    let result = shortest
    for(let i = 0; i < strs.length; i++) {
        for(let j = 0; j < result.length; j++) {
            if(result[j] !== strs[i][j]) {
                result = result.slice(0, j)
                break
            }
        }
    }
    return result
};