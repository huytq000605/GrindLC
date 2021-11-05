/**
 Do not return anything, modify nums in-place instead.
 */
 function rotate(nums: number[], k: number): void {
    k = k % nums.length
    let reverse = (start: number, end: number) => {
        while(start < end) {
            [nums[start], nums[end]] = [nums[end], nums[start]];
            start++
            end--
        }
    }
    reverse(0, nums.length - 1)
    reverse(0, k - 1)
    reverse(k, nums.length - 1)
    
};