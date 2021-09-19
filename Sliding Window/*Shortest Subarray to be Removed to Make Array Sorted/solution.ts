function findLengthOfShortestSubarray(arr: number[]): number {
    let left = 0
    for(; left < arr.length - 1; left++) { // Delete all from left + 1 to end
        if(arr[left] > arr[left + 1]) {
            break
        }
    }
    if(left === arr.length - 1) return 0
    
    let right = arr.length - 1
    for(; right > 0; right--) { // Delete from all right - 1 to 0
        if(arr[right] < arr[right - 1]) {
            break
        }
    }
    
    let result = Math.min(arr.length - 1 - (left + 1) + 1, right)
    let i = 0
    while(i <= left && right < arr.length) { // Try to delete at middle of the array
        if(arr[i] <= arr[right]) {
            result = Math.min(result, right - 1 - (i + 1) + 1)
            i++
        } else {
            right++
        }
    }
    
    return result
    
};