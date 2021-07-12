function permute(nums: number[]): number[][] {
    let result = []
    helper(nums, 0, [], result)
    return result
};

function helper(nums: number[], index: number, current: number[], result: number[][]) {
    if(current.length === nums.length) {
        result.push([...current])
        return
    }
    for(let i = index; i < nums.length; i++) {
        current.push(nums[i]);
        [nums[i], nums[index]] = [nums[index], nums[i]];
        helper(nums, index + 1, current, result);
        [nums[i], nums[index]] = [nums[index], nums[i]];
        current.pop()
    }
}