function maximumBeauty(items: number[][], queries: number[]): number[] {
    let result = Array(queries.length).fill(0)
    items.sort((a,b) => a[0] - b[0])
    let cache = new Map()
    let max = 0
    for(let [price, beauty] of items) {
        max = Math.max(max, beauty)
        cache.set(price, max)
    }
    let keys = Array.from(cache.keys())
    for(let [idx, query] of queries.entries()) {
        let min = 0
        let max = cache.size - 1
        while(min < max) {
            let mid = min + Math.ceil((max - min + 1) / 2)
            if(keys[mid] <= query) {
                min = mid
            } else {
                max = mid - 1 
            }
        }
        if(keys[min] <= query) {
            result[idx] = cache.get(keys[min])
        }
    }
    return result
              
};