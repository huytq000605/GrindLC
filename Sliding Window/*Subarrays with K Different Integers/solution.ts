function subarraysWithKDistinct(nums: number[], k: number): number {
    let atMostK = (k: number) => { // Number of sliding window has at most k different integers
        let map = new Map()
        let start = 0
        let result = 0
        for(let i = 0; i < nums.length; i++) {
            map.set(nums[i], (map.get(nums[i]) || 0) + 1)
            while(map.size > k) {
                map.set(nums[start], map.get(nums[start]) - 1)
                if(map.get(nums[start]) === 0) map.delete(nums[start])
                start++
            }
            result += i - start + 1
        }
        return result
    }
    return atMostK(k) - atMostK(k-1)
};