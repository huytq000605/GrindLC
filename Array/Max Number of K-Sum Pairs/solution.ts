function maxOperations(nums: number[], k: number): number {
    let map = new Map()
    let result = 0
    for(let i = 0; i < nums.length; i++) {
        if(map.get(nums[i]) > 0) {
            map.set(nums[i], map.get(nums[i]) - 1)
            result++
            continue;
        }
        map.set(k-nums[i], (map.get(k-nums[i]) || 0) + 1)
    }
    return result
};