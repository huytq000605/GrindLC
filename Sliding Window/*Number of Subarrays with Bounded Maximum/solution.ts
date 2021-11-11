function numSubarrayBoundedMax(nums: number[], left: number, right: number): number {
    let count = (k: number) => {
        let start = 0
        let result = 0
        for(let i = 0; i < nums.length; i++) {
            if(nums[i] > k) {
                start = i + 1
                continue
            }
            result += i - start + 1
        }
        return result
    }
    return count(right) - count(left - 1)
};