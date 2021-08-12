function totalFruit(fruits: number[]): number {
    let map = new Map()
    let result = 0
    let start = 0
    for(let i = 0; i < fruits.length; i++) {
        map.set(fruits[i], (map.get(fruits[i]) || 0) + 1)
        while(map.size > 2) {
            let currentValue = map.get(fruits[start])
            if(currentValue > 1) {
                map.set(fruits[start], currentValue - 1)
            } else {
                map.delete(fruits[start])
            }
            start++
        }
        result = Math.max(result, i - start + 1)
    }
    return result
};