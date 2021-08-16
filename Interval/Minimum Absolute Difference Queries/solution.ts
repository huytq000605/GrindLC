function minDifference(nums: number[], queries: number[][]): number[] {
    let max = 1;
    for(let num of nums) {
        max = Math.max(num, max)
    }
    let prefix = Array(nums.length).fill(0).map(() => Array(max).fill(0))
    for(let i = 0; i < nums.length; i++) {
        if(i === 0) {
            prefix[0][nums[i] - 1]++
        } else {
            for(let j = 0; j < max; j++) {
                prefix[i][j] = prefix[i-1][j]
            }
            prefix[i][nums[i] - 1]++
        }
    }
    let arr = Array(max) 
    let result = Array(queries.length)
    for(let [idx, query] of queries.entries()) {
        for(let i = 0; i < arr.length; i++) {
            if(query[0] > 0) {
                arr[i] = prefix[query[1]][i] - prefix[query[0] - 1][i]
            } else {
                arr[i] = prefix[query[1]][i]
            }
            
        }
        result[idx] = cal(arr)
    }
    return result
};

function cal(arr) {
    let result = Number.MAX_SAFE_INTEGER
    let prev = -1
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] > 0) {
            if(prev !== -1) {
                result = Math.min(result, i - prev)
                prev = i
            } else {
                prev = i
            }
        }
    } 
    if(result === Number.MAX_SAFE_INTEGER) return -1
    return result
}

