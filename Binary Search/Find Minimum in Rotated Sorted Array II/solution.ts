function findMin(nums: number[]): number {
    let findMinPartition = (start, end) => {
        if(start > end) return Number.MAX_SAFE_INTEGER
        if(nums[start] < nums[end]) {
            return nums[start]
        } else {
            let min = start
            let max = end
            while(min < max) {
                let mid = min + Math.floor((max - min) / 2)
                if(nums[mid] < nums[0]) {
                    max = mid
                } else if(nums[mid] > nums[0]) {
                    min = mid + 1
                } else { 
					// Testcase: 1 1 1 1 1 1 0 1 1 1 1 1 1 1
					// We don't know that where is the partition of min number
                    return Math.min(findMinPartition(min, mid), findMinPartition(mid + 1, max))
                }
            }
            return nums[min]
        }
    }
    return findMinPartition(0, nums.length - 1)
};
