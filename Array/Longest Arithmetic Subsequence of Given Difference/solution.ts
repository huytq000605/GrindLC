function longestSubsequence(arr: number[], difference: number): number {
    let map = new Map()
    let result = 1
    for(let i = 0; i < arr.length; i++) {
        map.set(arr[i], (map.get(arr[i] - difference) || 0) + 1)
        result = Math.max(result, map.get(arr[i]))
    }
    return result
};