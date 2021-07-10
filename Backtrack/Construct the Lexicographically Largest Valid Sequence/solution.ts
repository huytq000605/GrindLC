function constructDistancedSequence(n: number): number[] {
    let result = Array((n-1) * 2 + 1).fill(0)
    let nums = Array(n).fill(0).map((_, idx) => n - idx)
    let seen = new Set()
    function helper(num: number, index: number) {
        if(index >= result.length) return false
        if(num !== 1 && num + index >= result.length) {
            return false
        }
        if(result[index] !== 0 || (num !== 1 && result[index + num] !== 0)) {
            return false
        }
        
        result[index] = num
        if(num !== 1) {
            result[index + num] = num
        }
        seen.add(num)
        if(seen.size === nums.length) { // We found a satisfied string, return true
            return true
        }
        let newIndex = index
        while(result[newIndex] !== 0 && newIndex < result.length) { // Find unfill index
            newIndex++
        }
        for(let n of nums) { // Loop through all possible
            if(!seen.has(n) ) {
                if(helper(n, newIndex) === true) return true // If we found a satisfied just return true, no need  to loop more
            }
        }
        result[index] = 0
        if(num !== 1) {
            result[index + num] = 0
        }
        
        seen.delete(num)
    }
    helper(nums[0], 0)
    return result
};