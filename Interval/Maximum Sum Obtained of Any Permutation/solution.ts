function maxSumRangeQuery(nums: number[], requests: number[][]): number {
    let line = Array(nums.length + 1).fill(0)
    for(let request of requests) {
        let [start, end] = request
        line[start]++
        line[end + 1]--
    }
    
    let prefix = Array(nums.length).fill(0)
    for(let i = 0; i < prefix.length; i++) {
        if(i === 0) prefix[i] = line[i]
        else prefix[i] = prefix[i-1] + line[i]
    }
    prefix.sort((a,b) => a-b)
    nums.sort((a,b) => a-b)
    let result = 0
    for(let i = 0; i < nums.length; i++) {
        result += prefix[i] * nums[i]
        result = result % (1e9 + 7)
    }
    return result
};