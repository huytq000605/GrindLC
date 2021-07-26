function maximumSwap(num: number): number {
    let arr = String(num).split("")
    let maxNum = Array(arr.length).fill(0)
    for(let i = arr.length -1; i >= 0; i--) {
        if(i === arr.length - 1) {
            maxNum[i] = [arr[i], i]
        } else {
            if(arr[i] > maxNum[i + 1][0]) maxNum[i] = [arr[i], i]
            else maxNum[i] = maxNum[i + 1]
        }
    }
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] < maxNum[i][0]) {
            let idx = maxNum[i][1];
            [arr[i], arr[idx]] = [arr[idx], arr[i]];
            break
        }
    }
    return Number(arr.join(""))
};


// 1294