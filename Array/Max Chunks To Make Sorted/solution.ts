function maxChunksToSorted(arr: number[]): number {
    let startNumber = 0;
    let startIndex = 0
    let endNumber = -1
    let result = 0
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] > endNumber) {
            endNumber = arr[i]
        }
        if(endNumber - startNumber + 1 == i - startIndex + 1) {
            result++
            startNumber = endNumber + 1;
            startIndex = i + 1
            endNumber = -1
        }
    }
    return result
};