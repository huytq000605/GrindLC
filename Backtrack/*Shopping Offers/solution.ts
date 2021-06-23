function shoppingOffers(price: number[], special: number[][], needs: number[]): number {
    let cache = new Map()
    function shopping(needs: number[], current: number) {
        const key = JSON.stringify(`${needs}${current}`)
        if(cache.has(key)) {
            return cache.get(key)
        }
        
        // Assign result to the case if we buy everything with basic price
        let result = current
        for(let i = 0; i< needs.length; i++) {
            result += needs[i] * price[i]
        }

        for(let spec of special) { // Try to buy every special deal ( then dfs for each valid buy )
            let validBuy = true
            for(let i = 0; i < needs.length; i++) {
                if(spec[i] > needs[i]) {
                    validBuy = false
                    break
                }
            }
            if(validBuy) {
                let needsAfterBuy = Array(needs.length)
                for(let i = 0; i < needsAfterBuy.length; i++) {
                    needsAfterBuy[i] = needs[i] - spec[i]
                }
                result = Math.min(shopping(needsAfterBuy, current + spec[spec.length - 1]), result)
            }
        }
        
        cache.set(key, result)
        return result
    }
    return shopping(needs, 0)
};
