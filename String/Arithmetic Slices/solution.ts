function numberOfArithmeticSlices(nums: number[]): number {
    if(nums.length < 3) return 0;
    let result = 0;
    // First we save the difference of each element in nums[i] compare with nums[i-1] into an arr call dp
    let dp = Array(nums.length - 1);
    for(let i = 1; i < nums.length; i++) {
        dp[i-1] = nums[i] - nums[i-1];
    }
    let current = dp[0];
    let count = 1; // count how many element of dp equal to previous
    // LIKE IF WE HAVE [1,2,3,4,6,8,9]
    // THEN THE DP is  [1,1,1,2,2,1]
    // We loop through the dp array to find how many continous equal element, if > 1 then there are >= 3 element
    for(let i = 1; i < dp.length; i++) {
        if(dp[i] === current) {
            count++;
        } else {
            if(count > 1) {
                result += helper(count)
            }
            current = dp[i];
            count = 1;
        }
    }
    // FOR THE LAST that we didnt count when loop ended
    if(count > 1) {
        result += helper(count)
    }
    return result;
};

// FROM THE EXAMPLE, IF DP is [1,1,1,2,2,1], the result can make from dp[0], dp[1] && dp[0], dp[1], dp[2] && dp[1], dp[2] and continue ...
function helper(count) {
    let result = 0
    for(let i = 0; i < count - 1; i++) {
        for(let j = i + 1; j < count; j++) {
            result++
        }
    }
    return result
}
