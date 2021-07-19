// We observer that the last element only > the first element when it's in the original order. Then we return the first element
// Else we just need to find the first index that arr[index] < arr[0]
function findMin(nums: number[]): number {
    if(nums[nums.length - 1] > nums[0]) {
        return nums[0]
    }
    let min = 0
    let max = nums.length - 1
    while(min < max) {
        let mid = min + Math.floor((max - min) / 2)
        if(nums[mid] < nums[0]) {
            max = mid
        } else {
            min = mid + 1
        }
    }
    return nums[min]
};


// 1 2 3 4 5 
// 5 1 2 3 4
// 4 5 1 2 3
// 3 4 5 1 2 
// 2 3 4 5 1
// 1 2 3 4 5