function maxLength(arr: string[]): number {
    let strs = []
    for(let i = 0; i < arr.length; i++) {
        let valid = true
        let str = Array(26).fill(0)
        for(let j = 0; j < str.length; j++) {
            let idx = arr[i].charCodeAt(j) - "a".charCodeAt(0)
            str[idx]++
            if(str[idx] === 2) {
                valid = false
                break
            }
        }
        if(valid) strs.push(str)
    }
    
    let result = 0
    let current = Array(26).fill(0)
    let dfs = (idx) => {
        if(idx >= strs.length) return
        dfs(idx + 1) // Pass this string
        if(check(current, strs[idx])) { // If can add, try to add
            for(let i = 0; i < 26; i++) {
                current[i] += strs[idx][i]
            }
            result = Math.max(result, count(current))
            dfs(idx + 1)
            for(let i = 0; i < 26; i++) {
                current[i] -= strs[idx][i]
            }
        }
    }
    
    dfs(0)
    return result
};

function check(str1, str2) {
    for(let i = 0; i < 26; i++) {
        if(str1[i] === 1 && str2[i] === 1) return false
    }
    return true
}

function count(str) {
    let result = 0
    for(let l of str) {
        if(l === 1) result++
    }
    return result
}