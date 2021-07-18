function findDiagonalOrder(nums: number[][]): number[] {
    let diagonal = new Map()
    for(let i = 0; i < nums.length; i++) {
        for(let j = 0 ; j < nums[i].length; j++) {
            if(!diagonal.has(i + j)) diagonal.set(i + j, [])
            diagonal.get(i + j).push(nums[i][j])
        }
    }
    let result = []
    for(let key of diagonal.keys()) {
        let arr = diagonal.get(key)
        for(let i = arr.length - 1; i >= 0; i--){
            result.push(arr[i])
        }
    }
    return result
};