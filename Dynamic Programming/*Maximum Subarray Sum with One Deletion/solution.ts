function maximumSum(arr: number[]): number {
    let maxEndHere = Array(arr.length)
    let maxStartHere = Array(arr.length)
    maxEndHere[0] = arr[0]
    maxStartHere[arr.length - 1] = arr[arr.length - 1]
    for(let i = 1; i < arr.length; i++) {
        maxEndHere[i] = Math.max(arr[i], maxEndHere[i-1] + arr[i])
    }
    for(let i = arr.length - 2; i >= 0; i--) {
        maxStartHere[i] = Math.max(arr[i], maxStartHere[i + 1] + arr[i])
    }
    let result = 0
    result = Math.max(...maxEndHere) // No deletion
    if(arr.length > 1) {
        for(let i = 0; i < arr.length; i++) { // i is the index we will delete
            if(i > 0 && i < arr.length - 1) {
                result = Math.max(result, maxEndHere[i-1] + maxStartHere[i+1])
            } else if(i === 0) {
                result = Math.max(result, maxStartHere[1])
            } else if(i === arr.length - 1) {
                result = Math.max(result, maxEndHere[arr.length - 1])
            }
        }
    }
    
    return result
};