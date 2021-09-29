// Same as permutation
// From right to left, find the first arr[i] that arr[i] < arr[i-1], i = swap
// Find the right most element that arr[swap] < arr[find]
// Swap two element
// Reverse from index swap to end

function nextGreaterElement(n: number): number {
    let arr = String(n).split("")
    for(let i = arr.length - 2; i >= 0; i--) {
        if(arr[i] < arr[i + 1]) {
            let swap = i
            for(let j = arr.length - 1; j > swap; j--) {
                if(arr[j] > arr[swap]) {
                    [arr[j], arr[swap]] = [arr[swap], arr[j]]
                    let result = ""
                    for(let k = 0; k <= swap; k++) result += arr[k]
                    for(let k = arr.length - 1; k > swap; k--) result += arr[k]
                    if(Number(result) > Math.pow(2,31) - 1) return -1
                    return Number(result)
                }
            }
        }
    }
    return -1
};