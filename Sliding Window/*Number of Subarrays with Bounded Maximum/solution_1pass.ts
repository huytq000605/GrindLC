function numSubarrayBoundedMax(nums: number[], left: number, right: number): number {
    let start = 0;
    let max = 0
    let result = 0
    let latestNumsLowerThanLeft = 0
    for(let i = 0; i < nums.length; i++) {
        if(nums[i] >= left) {
            latestNumsLowerThanLeft = 0
        }
        max = Math.max(nums[i], max)
        if(max >= left && max <= right) {
            if(nums[i] < left) latestNumsLowerThanLeft++
            result += i - start + 1 - latestNumsLowerThanLeft
			// Every new subarray we all will be [nums[start], ..., nums[i]], [nums[start + 1], ..., nums[i]], ... , [nums[i]] =>
			// So if example we have 2 latestNumsLowerThanLeft then nums[i] & nums[i - 1] will be < left
			// So [nums[i-1], nums[i]], [nums[i]] is not satisfy
        }
        if(max > right) {
            start = i + 1
            max = 0
            latestNumsLowerThanLeft = 0
        }
    }
    return result
};