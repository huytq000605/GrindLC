// Find the first min element, then have two sorted arrays
function search(nums: number[], target: number): number {
    let first = 0
    if(nums[first] > nums[nums.length - 1]) {
        let min = 0
        let max = nums.length - 1
        while(min < max) {
            let mid = min + Math.floor((max - min)/ 2)
            if(nums[mid] < nums[0]) {
                max = mid
            } else {
                min = mid + 1
            }
        }
        first = min
    }
    if(target === nums[first]) return first
    if(target < nums[first]) return -1
    
    let min = 0
    let max = first - 1
    while(min < max) {
        let mid = min + Math.floor((max - min)/ 2)
        if(nums[mid] === target) return mid
        if(nums[mid] < target) {
            min = mid + 1
        } else {
            max = mid - 1
        }
    }
    if(nums[min] === target) return min
    
    min = first + 1
    max = nums.length - 1
    while(min < max) {
        let mid = min + Math.floor((max - min)/ 2)
        if(nums[mid] === target) return mid
        if(nums[mid] < target) {
            min = mid + 1
        } else {
            max = mid - 1
        }
    }
    if(nums[min] === target) return min
    return -1
    
};