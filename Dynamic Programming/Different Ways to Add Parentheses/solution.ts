function diffWaysToCompute(expression: string): number[] {
    let current = 0
    let arr = []
    for(let l of expression) {
        if(l >= "0" && l <= "9") {
            current = current * 10 + Number(l)
        } else {
            arr.push(current)
            arr.push(l)
            current = 0
        }
    }
    arr.push(current)
    
    let dp = Array(arr.length).fill(0).map(() => Array(arr.length))
    let dfs = (start, end) => {
        if(start === end) {
            return [arr[start]]
        }
        if(dp[start][end] !== undefined) return dp[start][end]
        let result = []
        for(let i = start + 1; i < end; i+= 2) {
            let prevs = dfs(start, i - 1)
            let afters = dfs(i + 1, end)
            for(let prev of prevs) {
                for(let after of afters) {
                    switch(arr[i]) {
                        case "+": 
                            result.push(prev + after)
                            break
                        case "-":
                            result.push(prev - after)
                            break
                        case "*":
                            result.push(prev * after)
                            break
                    }
                }
            }
        }
        dp[start][end] = result
        return result
    }
    return dfs(0, arr.length - 1)
};