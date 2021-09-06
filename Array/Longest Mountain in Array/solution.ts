function longestMountain(arr: number[]): number {
    let start = 0
    let result = 0
    for(let i = 0; i < arr.length; i++) {
        if(i + 1 < arr.length && arr[i] >= arr[i+1]) {
            if(arr[i+1] === arr[i]) { // Equal cannot be moutain
                start = i + 1
                continue
            }
            if(i - start + 1 === 1) { // Dont have any element on the left of top
                start = i + 1
            } else {
                let right = 0 // Count how many elements on the right of top
                i += 1
                while(i < arr.length && arr[i] < arr[i-1]) {
                    right++
                    i++
                }
                if(right > 0) {
                    result = Math.max(result, i - start)
                }
                start = i-1 // new start is the last element on the right
                i-=2 // At the end of loop, i will + 1 so - 2
                
            }
        }
    }
    return result
};