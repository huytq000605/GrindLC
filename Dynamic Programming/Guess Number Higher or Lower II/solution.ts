function getMoneyAmount(n: number): number {
    let cache = Array(n + 1).fill(0).map(() => Array(n + 1))
    let buildTree = (start, end) => {
        if(start >= end) return 0
        if(cache[start][end] !== undefined) return cache[start][end]
        let result = Number.MAX_SAFE_INTEGER
        for(let i = start; i <= end; i++) {
            let mid = i
            let left = buildTree(start, i - 1)
            let right = buildTree(i + 1, end)
            result = Math.min(result, Math.max(mid + left, mid + right))
        }
        cache[start][end] = result
        return result
    }  
    return buildTree(1, n)
};