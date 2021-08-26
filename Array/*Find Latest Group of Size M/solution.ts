function findLatestStep(arr: number[], m: number): number {
    let count = Array(arr.length + 2).fill(0)
    let length = Array(arr.length + 1).fill(0)
    let result = -1
    for(let i = 0; i < arr.length; i++) {
        let left = count[arr[i] - 1]
        if(left > 0) length[left]--
        let right = count[arr[i] + 1]
        if(right > 0) length[right]--
        let newLength = left+right+1
        count[arr[i] - left] = newLength
        count[arr[i] + right] = newLength
        length[newLength]++
        if(length[m] > 0) result = i + 1
    }
    return result
};