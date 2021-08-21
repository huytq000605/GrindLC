function numTilings(n: number): number {
    let cache = Array(1001).fill(0).map(() => Array(1001))
    let MOD = 1e9 + 7
    let helper = (top: number, bottom: number) => {
        if(top < 0 || bottom < 0) return 0
        if(top === 0 && bottom === 0) return 1
        if(cache[top][bottom] !== undefined) return cache[top][bottom]
        let result = 0
        if(top === bottom) {
            result += helper(top - 1, bottom - 1)
            result += helper(top - 2, bottom - 1)
            result += helper(top - 1, bottom - 2)
            result += helper(top - 2, bottom - 2)
        }
        if(top === bottom - 1) {
            result += helper(top - 1, bottom - 2)
            result += helper(top, bottom - 2)
        }
        if(top === bottom + 1) {
            result += helper(top - 2, bottom)
            result += helper(top - 2, bottom - 1)
        }
        result = result % MOD
        cache[top][bottom] = result
        return result
    }
    return helper(n, n)
};