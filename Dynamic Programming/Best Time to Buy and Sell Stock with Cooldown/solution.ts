function maxProfit(prices: number[]): number {
    let cache = new Map()
    function helper(index: number, buy: boolean, cooldown: boolean) {
        if(index === prices.length) return 0
        const key = `${index}-${buy}-${cooldown}`
        if(cache.has(key)) return cache.get(key)
        if(!buy) {
            let passThis = helper(index + 1, false, false)
            if(cooldown) {
                cache.set(key, passThis)
            } else {
                let buyThis = -prices[index] + helper(index, true, false)
                cache.set(key, Math.max(buyThis, passThis))
            }
        }
        if(buy) {
            let sellThis = prices[index] + helper(index + 1, false, true)
            let passThis = helper(index + 1, true, false)
            cache.set(key, Math.max(sellThis, passThis))
        }
        return cache.get(key)
    }
    return helper(0, false, false)
}

