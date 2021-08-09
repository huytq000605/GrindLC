function findMaxForm(strs: string[], m: number, n: number): number {
    let arr = strs.map((str) => {
        let result = [0, 0]
        for(let c of str) {
            if(c === "0") result[0]++
            else result[1]++
        }
        return result
    })
    
    let cache = Array(strs.length).fill(0).map(() => Array(m + 1).fill(0).map(() => Array(n + 1)))
    
    let helper = (index, m, n) => {
        if(index >= strs.length) return 0
        if(cache[index][m][n] !== undefined) return cache[index][m][n]
        let result = 0
        for(let i = index; i < strs.length; i++) {
            if(m >= arr[i][0] && n >= arr[i][1]) {
                result = Math.max(result, 1 + helper(i + 1, m - arr[i][0], n - arr[i][1]))
            }
        }
        cache[index][m][n] = result
        return result
    } 
    
    return helper(0, m, n)
};

