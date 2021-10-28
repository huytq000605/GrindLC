function threeSum(nums: number[]): number[][] {
    nums.sort((a,b) => a-b)
    let result = []
    for(let i = 0; i < nums.length; i++) {
        if(i > 0 && nums[i] === nums[i-1]) continue
        let left = i + 1
        let right = nums.length - 1
        let sum = -nums[i]
        while(left < right) {
            if(nums[left] + nums[right] < sum) {
                left++
            } else if(nums[left] + nums[right] > sum) {
                right--
            } else {
                result.push([nums[i], nums[left], nums[right]])
                let currentLeft = nums[left]
                while(left < right && nums[left] === currentLeft)
                    left++
            }
        }
    }
    return result
};