function search(nums: number[], target: number): boolean {
    let start = 0
    let end = nums.length -1
    while(start <= end) {
        let mid = start + Math.floor((end - start) / 2)
        if(nums[mid] === target) return true
		// Different from problem I
        while(start !== mid && nums[start] === nums[mid]) {
            start++
        }
        while(end !== mid && nums[end] === nums[mid]) {
            end--
        }
		//
        if(nums[mid] >= nums[start]) {
            if(nums[start] <= target && target < nums[mid]) {
                end = mid - 1
            } else {
                start = mid + 1
            }
        } else {
            if(nums[mid] < target && target <= nums[end]) {
                start = mid + 1
            } else {
                end = mid - 1
            }
        }
    }
    return false
};