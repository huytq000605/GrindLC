function maxProfitAssignment(difficulty: number[], profit: number[], worker: number[]): number {
    let arr = Array(profit.length).fill(0).map((e, i) => [difficulty[i], profit[i]]).sort((a,b) => a[1]-b[1])
    worker.sort((a,b) => a-b)
    let result = 0
    while(worker.length && arr.length) {
        if(arr[arr.length - 1][0] > worker[worker.length - 1]) {
            arr.pop()
        } else {
            worker.pop()
            result += arr[arr.length - 1][1]
        }
    } 
    return result
};