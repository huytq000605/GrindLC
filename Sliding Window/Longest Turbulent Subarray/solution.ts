function maxTurbulenceSize(arr: number[]): number {
    if(arr.length === 1) return 1
    let result = 1
    let start = 0
    let lessThanNext = true
	// Initial value for lessThanNext
    if(arr[0] > arr[1]) {
        lessThanNext = false
    } else {
        lessThanNext = true
    }
	// Loop through arr
    for(let end = 0; end < arr.length - 1; end++) {
        if(arr[end] === arr[end + 1]) { // If we have adjacency, we need to start from the later one
            start = end + 1
            continue
        }
        if(lessThanNext) {
            if(arr[end] < arr[end + 1]) {
                result = Math.max(result, end + 1 - start + 1)
                lessThanNext = !lessThanNext
            } else {
                start = end
                lessThanNext = true
            }
        } else {
            if(arr[end] > arr[end + 1]) {
                result = Math.max(result, end + 1- start + 1)
                lessThanNext = !lessThanNext
            } else {
                lessThanNext = false
                start = end
            }
        }
    }
    return result
};