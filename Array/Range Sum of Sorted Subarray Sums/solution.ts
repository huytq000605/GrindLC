function rangeSum(nums: number[], n: number, left: number, right: number): number {
    let totals = []
    let result = 0
    for(let i = 0; i < nums.length; i++) {
        helper(nums, i, 0, totals)
    }
    totals.sort((a,b)=>a-b)
    for(let i = left - 1; i < right; i++) {
        result += totals[i]
    }
    return result%1000000007
    
};

function helper(nums, index, current, totals) {
    if(index === nums.length) return;
    current += nums[index]
    totals.push(current)
    helper(nums, index + 1, current, totals)
}