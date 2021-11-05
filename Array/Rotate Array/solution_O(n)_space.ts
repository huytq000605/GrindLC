/**
 Do not return anything, modify nums in-place instead.
 */
 function rotate(nums: number[], k: number): void {
    k = k % nums.length
    let breakPoint = nums.length - k
    let result = [...nums.slice(breakPoint), ...nums.slice(0, breakPoint)]
    for(let i = 0; i < nums.length; i++) nums[i] = result[i]
};