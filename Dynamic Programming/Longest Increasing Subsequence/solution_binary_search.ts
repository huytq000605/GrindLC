function lengthOfLIS(nums: number[]): number {
    let res = []
    for(let num of nums) {
        let min = 0
        let max = res.length - 1
        while(min < max) {
            let mid = min + Math.floor((max - min)/ 2)
            if(res[mid] >= num) { // Find the first number in res that >= num to replace
				// Idea from Increasing Triplet Subsequence
                max = mid
            } else {
                min = mid + 1
            }
        }
        if(res[min] >= num) {
            res[min] = num
        } else {
            res.push(num)
        }
    }
    return res.length
};

