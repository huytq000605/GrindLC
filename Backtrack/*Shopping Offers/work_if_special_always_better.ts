function shoppingOffers(price: number[], special: number[][], needs: number[]): number {
    let cache = new Map()
    function shopping(needs, current) {
        const key = JSON.stringify(`${needs}${current}`)
        if(cache.has(key)) {
            return cache.get(key)
        }
        let flag = false
        let result = Number.MAX_SAFE_INTEGER
        for(let spec of special) {
            let validBuy = true
            for(let i = 0; i < needs.length; i++) {
                if(spec[i] > needs[i]) validBuy = false
            }
            if(validBuy) {
                let needsAfterBuy = Array(needs.length)
                for(let i = 0; i < needsAfterBuy.length; i++) {
                    needsAfterBuy[i] = needs[i] - spec[i]
                }
                flag = true
                result = Math.min(shopping(needsAfterBuy, current + spec[spec.length - 1]), result)
            }
        }
        if(!flag) {
            let plus = 0;
            for(let i = 0; i< needs.length; i++) {
                if(needs[i] > 0) {
                    plus += needs[i] * price[i]
                }
            }
            result = Math.min(result, current + plus)   
        }
        
        cache.set(key, result)
        return result
    }
    return shopping(needs, 0)
};
