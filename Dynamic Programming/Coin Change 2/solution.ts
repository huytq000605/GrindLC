// Can use JSON.stringify array to be key but this is optimized version

function change(amount: number, coins: number[]): number {
    let map = new Map()
    function helper(amount: number, index: number): number {
        let key = `${amount}-${index}`
        if(map.has(key)) {
            return map.get(key)
        }
        if(amount === 0) {
            return 1
        }
        if(amount < 0 || index === coins.length) {
            return 0
        }
        map.set(key, helper(amount - coins[index], index) + helper(amount, index + 1))
        return map.get(key)
    }
    return helper(amount, 0)
};

