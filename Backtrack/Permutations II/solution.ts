function permuteUnique(nums: number[]): number[][] {
    let result = []
    helper(nums, 0, [], result)
    return result
};

function helper(nums: number[], index: number, current: number[], result: number[][]) {
    if(current.length === nums.length) {
        result.push([...current])
        return
    }
    let set = new Set()
    for(let i = index; i < nums.length; i++) {
        if(set.has(nums[i])) continue
        set.add(nums[i])
        current.push(nums[i]);
        [nums[i], nums[index]] = [nums[index], nums[i]];
        helper(nums, index + 1, current, result)
        current.pop();
        [nums[i], nums[index]] = [nums[index], nums[i]];
    }
}