function longestMountain(arr: number[]): number {
    let up = 0;
    let down = 0
    let result = 0
    for(let i = 1; i < arr.length; i++) {
        if(arr[i-1] === arr[i] || (arr[i-1] > arr[i] && up === 0) ) {
            up = 0
            down = 0
        } else if(arr[i - 1] < arr[i]) {
            if(down > 0) {
                down = 0
                up = 0
            }
            up++
        } else if(arr[i - 1] > arr[i]) {
            down++
        }
        if(up > 0 && down > 0 && up + down + 1 > result) result = up + down + 1
        
    }
    return result
};