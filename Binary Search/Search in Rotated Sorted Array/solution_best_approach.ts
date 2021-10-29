// Best approach but difficult to understand
// Since it is the rotated sorted array => Each time we choose a middle index
// We got at least a sorted array in 1 side, check where is sorted side
// Check if target in the range of sorted side, if not => search for other side
function search(nums: number[], target: number): number {
    let min = 0
    let max = nums.length - 1
    while(min <= max) {
        // Since we leaning to left, then we check if the left list is sorted first
        let mid = min + Math.floor((max - min) / 2)
        if(nums[mid] === target) return mid
        if(nums[mid] >= nums[min]) { // Sorted list is on the left
            if(target >= nums[min] && target < nums[mid]) {
                max = mid - 1
            } else {
                min = mid + 1
            }
        } else { // Sorted list is on the right
            if(target > nums[mid] && target <= nums[max]) {
                min = mid + 1
            } else {
                max = mid - 1
            }
        }
    }
    return -1
};