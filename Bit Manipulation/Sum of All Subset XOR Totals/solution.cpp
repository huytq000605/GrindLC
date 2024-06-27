class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        // let's assume we have k nums that have ith bit set to 1
        // => n - k nums that have ith bit set to 0
        // => Number of times ith bit contribute to answer will be
        // comb(k, 1) + comb(k, 3) + ... = 2^(k-1) to select odd number of nums in k nums
        // 2^(n-k) to select the remaining nums
        // => total of 2^(n-1) subarrays
        // => each bit contribute 2^(n-1) times
        int bits = 0;
        for(int num: nums) { bits |= num; };
        return bits << (nums.size()-1);
    } 
};
