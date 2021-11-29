function minDistance(word1: string, word2: string): number {
    let dp = Array(word1.length).fill(0).map(() => Array(word2.length))
    let dfs = (idx1: number, idx2: number) => {
        if(idx1 >= word1.length && idx2 >= word2.length) {
            return 0
        }
        else if(idx1 >= word1.length) {
            return word2.length - idx2
        } else if(idx2 >= word2.length) {
            return word1.length - idx1
        }
        if(dp[idx1][idx2] !== undefined) return dp[idx1][idx2]
        let result
        if(word1[idx1] === word2[idx2]) {
            result = dfs(idx1 + 1, idx2 + 1)
        } else {
            let add = dfs(idx1, idx2 + 1) + 1
            let remove = dfs(idx1 + 1, idx2) + 1
            let replace = dfs(idx1 + 1, idx2 + 1) + 1
            result = Math.min(add, remove, replace)
        }
        dp[idx1][idx2] = result
        return result
    }
    return dfs(0, 0)
};