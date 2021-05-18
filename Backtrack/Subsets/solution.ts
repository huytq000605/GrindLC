function subsets(nums: number[]): number[][] {
    let result = [[]];
    helper(nums, 0, [], result)
    return result;
};
    
function helper(nums: number[], index: number, current: number[], result: number[][]) {
    if(index === nums.length) return;
    let i = index;
    while(i < nums.length) {
        current.push(nums[i]);
        result.push([...current]);
        helper(nums, ++i, current, result)
        current.pop();
    }
}