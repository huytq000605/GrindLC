function findBestValue(arr: number[], target: number): number {
    arr.sort((a,b) => a-b)
    let max = arr[arr.length - 1]
    let result = [Number.MAX_SAFE_INTEGER, -1]
    let prefix = Array(arr.length).fill(0)
    for(let i = 0; i < arr.length; i++) {
        if(i===0) prefix[i] = arr[0]
        else prefix[i] = prefix[i-1] + arr[i]
    }
    for(let choose = 0; choose <= max; choose++) {
        let min = -1
        let max = arr.length
        while(min < max) { // Binary Search to find the first element have value > choose
            let mid = min + Math.floor((max - min)/ 2)
            if (arr[mid] < choose) {
                min = mid + 1
            } else {
                max = mid
            }
        }
        let value
        if(min === -1) { // All element is > choose
            value = choose * arr.length
        } else if(min === arr.length) { // All element is <= choose
            value = prefix[arr.length - 1]
        } else {
            value = prefix[min - 1] + (arr.length - min) * choose
        }
        let diff = Math.abs(target- value)
        if(diff < result[0]) {
            result = [diff, choose]
        }
    }
    
    return result[1]
    
    
};