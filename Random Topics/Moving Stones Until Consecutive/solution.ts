function numMovesStones(a: number, b: number, c: number): number[] {
    let arr = [a,b,c]
    arr.sort((a,b) => a-b)
    let minMove = 0
    if(arr[0] + 1 === arr[1] && arr[1] + 1 === arr[2]) minMove = 0
    else if(arr[0] + 2 === arr[1] || arr[1] + 2 === arr[2] || arr[0] + 1 === arr[1] || arr[1] + 1 === arr[2]) minMove = 1
    else minMove = 2
    let maxMove = arr[1] - 1 - arr[0] + arr[2] - arr[1] - 1
    return [minMove,maxMove]
    
};