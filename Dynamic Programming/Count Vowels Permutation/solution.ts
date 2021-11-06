function countVowelPermutation(n: number): number {
    const MOD = 1e9 + 7
    let dict = {
        'e': ['a', 'i'],
        'a': ['u', 'i', 'e'],
        'i': ['o', 'e'],
        'u': ['o', 'i'],
        'o': ['i'],
    }
    let dp = Array(n).fill(0).map(() => new Map())
    let dfs = (index: number, previous: string) => {
        if(index >= n) return 1
        if(dp[index].get(previous) !== undefined) return dp[index].get(previous)
        let result = 0
        if(index === 0) {
            result = dfs(1, "a") + dfs(1, "e") + dfs(1, "o") + dfs(1, "u") + dfs(1, "i")
            result %= MOD
        } else {
            for(let letter of dict[previous]) {
                result += dfs(index + 1, letter)
                result %= MOD
            }
        }
        dp[index].set(previous, result)
        return result
    }
    
    return dfs(0, "")
};