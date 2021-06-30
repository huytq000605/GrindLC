function advantageCount(nums1: number[], nums2: number[]): number[] {
    nums1.sort((a,b) => a-b)
	// Sort nums2 and store the original index
    let nums = []
    for(let i = 0; i < nums2.length; i++) { 
        nums.push([i, nums2[i]])
    }
    nums.sort((a,b) => b[1] - a[1])
    let result = Array(nums1.length)
    let leftPointer = 0
    let rightPointer = nums1.length - 1
    for(let [idx, num] of nums) {
        if(num < nums1[rightPointer]) {
            result[idx] = nums1[rightPointer]
            rightPointer--
        } else {
            result[idx] = nums1[leftPointer]
            leftPointer++
        }
    }
    return result
};