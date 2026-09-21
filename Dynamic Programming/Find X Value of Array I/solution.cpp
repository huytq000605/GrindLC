class Solution {
public:
    vector<long long> resultArray(vector<int>& nums, int k) {
        vector<long long> result(k);
        vector<long long> dp(k);
        for(int num: nums) {
            num %= k;
            vector<long long> ndp(k);
            ndp[num] = 1;
            for(int j = 0; j < k; ++j) {
                ndp[(j*num)%k] += dp[j];
            }
            for(int j = 0; j < k; ++j) {
                result[j] += ndp[j];
            }
            dp = ndp;
        }
        return result;
    }
};
