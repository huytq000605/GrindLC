class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int s = accumulate(nums.begin(), nums.end(), 0);
        if(nums.empty() || s&1) return false;
        if(s == 0) return true;
        s >>= 1;
        bitset<20001> dp;
        dp[0] = 1;
        for(int &num: nums) {
            dp |= dp << num;
            if(dp[s]) return true;
        }
        return false;
    }
};
