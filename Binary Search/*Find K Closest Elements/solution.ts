// Sliding window arr[mid], arr[mid + 1],... arr[mid + k - 1], if |arr[mid] - x| < |arr[mid + k] - x| then arr[mid + 1], arr[mid + 2], ... arr[mid + k] is better than the previous one
// Take care for arr[mid] === arr[mid + k]

function findClosestElements(arr: number[], k: number, x: number): number[] {
    let min = 0
    let max = arr.length - k
    while(min < max) {
        let mid = min + Math.floor((max - min)/ 2)
        if(arr[mid] === arr[mid + k]) {
            if(arr[mid] < x) {
                min = mid
            } else if(arr[mid] > x) {
                max = mid
            } else {
                return arr.slice(mid, min + k)
            }
            continue
        } 
        if(Math.abs(arr[mid + k] - x) < Math.abs(arr[mid] - x)) {
            min = mid + 1
        } else {
            max = mid
        }
    }
    return arr.slice(min, min + k)
};
