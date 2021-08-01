function countSpecialSubsequences(nums: number[]): number {
    let cache = new Array(nums.length).fill(0).map(() => Array(3).fill(0).map(() => Array(2)))
    let module = 1000000007
    function helper(index, finding, haveFinding) {
        if(index === nums.length) {
            if(finding === 2 && haveFinding === true) {
                return 1
            } else {
                return 0
            }
        }
        if(cache[index][finding][haveFinding] !== undefined) {
            return cache[index][finding][haveFinding]
        }
        let result = 0
        if(!haveFinding) {
            if(nums[index] === finding) {
                result += helper(index + 1, finding, true)
            }
            result += helper(index + 1, finding, false)
        } else {
            if(nums[index] === finding) {
                result += helper(index + 1, finding, true)
            } else if(nums[index] === finding + 1) {
                result += helper(index + 1, finding + 1, true)
            }
            result += helper(index + 1, finding, true)
        }
        cache[index][finding][haveFinding] = result % module
        return result % module
        
    }
    
    return helper(0, 0, false)
};
