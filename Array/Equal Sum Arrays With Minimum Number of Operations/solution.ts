function minOperations(nums1: number[], nums2: number[]): number {
    let minSumNums1 = 1 * nums1.length
    let maxSumNums1 = 6 * nums1.length
    let minSumNums2 = 1 * nums2.length
    let maxSumNums2 = 6 * nums2.length
    if(minSumNums1 > maxSumNums2 || maxSumNums1 < minSumNums2) {
        return -1
    }
    let currentSum1 = 0
    let currentSum2 = 0
    for(let num of nums1) {
        currentSum1 += num
    }
    for(let num of nums2) {
        currentSum2 += num
    }
    let changes = new Map()
    let diff = 0
    if(currentSum2 < currentSum1) {
        [nums1, nums2] = [nums2, nums1]
        diff = currentSum1 - currentSum2
    } else {
        diff = currentSum2 - currentSum1
    }
    for(let num of nums1) {
        changes.set(6 - num, (changes.get(6-num) || 0) + 1 )
    }
    for(let num of nums2) {
        changes.set(num -1, (changes.get(num - 1) || 0) + 1)
    }
    let step = 0
    let change = 5
    while(diff > 0) {
        while(changes.get(change) > 0 && diff > 0) {
            changes.set(change, changes.get(change) - 1)
            diff = diff - change
            step++
        } 
        change--
    }
    return step

};