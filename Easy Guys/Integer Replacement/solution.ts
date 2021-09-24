function integerReplacement(n: number): number {
    let cache = new Map()
    let dfs = (n) => {
        if(n === 1) return 0
        if(n < 1) return Number.MAX_SAFE_INTEGER
        if(cache.has(n)) return cache.get(n)
        let result
        if(n % 2 === 0) result = dfs(n / 2) + 1
        else result = 1 + Math.min(dfs(n + 1), dfs(n-1))
        cache.set(n, result)
        return result
    }
    return dfs(n)
};