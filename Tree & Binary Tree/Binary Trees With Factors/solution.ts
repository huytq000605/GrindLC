function numFactoredBinaryTrees(arr: number[]): number {
    arr.sort((a, b) => b-a)
    let map = new Map()
    for(let i = 0; i < arr.length; i++) {
        map.set(arr[i], i)
    }

    let result = 0

    let cache = Array(arr.length)

    let construct = (index) => {
        if(cache[index] !== undefined) {
            return cache[index]
        }
        let result = 1
        for(let i = index + 1; i < arr.length; i++) {
            if(map.has(arr[index] / arr[i])) {
                result += (construct(i) * construct(map.get(arr[index] / arr[i])) ) % (1e9 + 7)
                result = result % (1e9 + 7)
            }
        }
        cache[index] = result
        return result
    }
    
    for(let i = 0; i < arr.length; i++) {
        result += construct(i) % (1e9 + 7)
        result = result % (1e9 + 7)
    }
    return result
    
};