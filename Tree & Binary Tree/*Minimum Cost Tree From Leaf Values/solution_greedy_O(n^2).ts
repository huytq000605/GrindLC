function mctFromLeafValues(arr: number[]): number {
    let result = 0
    while(arr.length >= 2) {
        let min = Math.min(...arr)
        let idx = arr.indexOf(min)
        if(idx === 0) result += arr[idx] * arr[idx + 1]
        else if(idx === arr.length - 1) result += arr[idx] * arr[idx - 1]
        else result += Math.min(arr[idx] * arr[idx - 1], arr[idx] * arr[idx + 1])
        arr.splice(idx, 1)
    }
    return result
};