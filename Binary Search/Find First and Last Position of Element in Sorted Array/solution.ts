function searchRange(nums: number[], target: number): number[] {
    let min = 0
    let max = nums.length - 1
    while(min < max) {
        let mid = min + Math.floor((max - min) / 2)
        if(nums[mid] < target) {
            min = mid + 1
        }
        if(nums[mid] > target) {
            max = mid - 1
        }
        if(nums[mid] === target) {
            max = mid
        }
    }
    if(nums[min] !== target) return [-1, -1]
    let result = [min, min]
    min = 0
    max = nums.length - 1
    while(min < max) {
        let mid = min + Math.ceil((max - min + 1) / 2)
        if(nums[mid] < target) {
            min = mid + 1
        }
        if(nums[mid] > target) {
            max = mid - 1
        }
        if(nums[mid] === target) {
            min = mid
        }
    }
    result[1] = min
    return result
};