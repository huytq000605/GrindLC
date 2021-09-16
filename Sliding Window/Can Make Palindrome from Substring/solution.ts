function canMakePaliQueries(s: string, queries: number[][]): boolean[] {
    let result = Array(queries.length)
    let check = (left, right, k) => {
        let arr = Array(26) 
        if(left === 0) arr = prefix[right]
        else {
            for(let i = 0; i < arr.length; i++) {
                arr[i] = prefix[right][i] - prefix[left-1][i]
            }
        }
        let count = 0
        for(let i = 0; i < arr.length; i++) {
            if(arr[i] % 2 === 1) {
                count++
            }
        }
        if(count - k * 2 > 1) return false
        return true
    }
    let prefix = Array(s.length).fill(0).map(e => Array(26))
    prefix[0] = Array(26).fill(0)
    for(let i = 0; i < s.length; i++) {
        if(i > 0) {
            for(let j = 0; j < 26; j++) {
                prefix[i][j] = prefix[i-1][j]
            }
        }
        prefix[i][s.charCodeAt(i) - "a".charCodeAt(0)]++
    }
    for(let i = 0; i < queries.length; i++) {
        let query = queries[i]
        let left = query[0]
        let right = query[1]
        let k = query[2]
        result[i] = check(left, right, k)
    }
    return result
};