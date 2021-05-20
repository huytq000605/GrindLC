/*
Key point to think about this question, because the array having only 1 non duplicate, so at the middle, if even index and the one next to it is equally then the non duplicate element must be on the right, and vice versa

*/


function singleNonDuplicate(nums: number[]): number {
    let min = 0;
    let max = nums.length - 1;
    while (min < max) {
        let middle = Math.floor((max+min)/2);
        if (middle % 2 === 1) {
            middle--
        }
        if (nums[middle + 1] !== nums[middle]) {
            max = middle;
        } else {
            min = middle +2 // We found a pair so just pass it
        }
        
    }
    return nums[min]
};