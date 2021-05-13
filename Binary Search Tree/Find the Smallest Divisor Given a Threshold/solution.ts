/*
Binary Search Tree
Think about min and max of the answer
*/
function smallestDivisor(nums: number[], threshold: number): number {
    let min = 1;
    let max = 0;
    for(let i = 0; i < nums.length; i++) {
        max = Math.max(max, nums[i])
    }
    while(min < max) {
        let mid = Math.floor((max+min) / 2);
        let sum = getSum(nums, mid);
        if(sum <= threshold) {
            max = mid;
        }
        else {
            min = mid + 1;
        }
    }
    return min
};

function getSum(nums: number[], divisor: number): number {
    let sum = 0;
    for(let i = 0; i < nums.length; i++) {
        sum += Math.ceil(nums[i]/divisor);
    }
    return sum;
}