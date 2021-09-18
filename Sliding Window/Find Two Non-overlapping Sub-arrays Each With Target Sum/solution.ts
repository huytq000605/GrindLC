function minSumOfLengths(arr: number[], target: number): number {
    let leftToRight = Array(arr.length).fill(Number.MAX_SAFE_INTEGER)
    let rightToLeft = Array(arr.length).fill(Number.MAX_SAFE_INTEGER)
    let map = new Map()
    map.set(0, -1)
    
    let sum = 0
    for(let i = 0; i < arr.length; i++) {
        sum += arr[i]
        if(i > 0) leftToRight[i] = leftToRight[i-1]
        if(map.has(sum - target)) {
            leftToRight[i] = Math.min(leftToRight[i], i - map.get(sum - target))
        }
        map.set(sum, i)
    }
    
    map.clear()
    sum = 0
    map.set(0, arr.length)
    
    for(let i = arr.length - 1; i >= 0; i--) {
        sum += arr[i]
        if(i < arr.length - 1) rightToLeft[i] = rightToLeft[i+1]
        if(map.has(sum - target)) {
            rightToLeft[i] = Math.min(rightToLeft[i], map.get(sum - target) - i)
        } 
        map.set(sum, i)
    }
    
    let result = Number.MAX_SAFE_INTEGER
    for(let i = 0; i < arr.length - 1; i++) {
        if(leftToRight[i] !== Number.MAX_SAFE_INTEGER && rightToLeft[i+1] !== Number.MAX_SAFE_INTEGER) {
            result = Math.min(result, leftToRight[i] + rightToLeft[i+1])
        }
    }
    if(result === Number.MAX_SAFE_INTEGER) return -1
    return result
};