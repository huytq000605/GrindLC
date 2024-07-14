class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        // dp[k][num] = maximum length of good subsequence that ends with num and having at most k idx that seq[i] != seq[i+1]
        vector<unordered_map<int, int>> dp(k+1);
        // res[k] = maximum length of good subsequence has at most k idxs that seq[i] != seq[i+1]
        vector<int> res(k+1);
        for(auto num: nums) {
            for(int i = k; i >= 0; i--) {
                dp[i][num] = max(i > 0 ? res[i-1] + 1 : 0, dp[i][num] + 1);
                res[i] = max(res[i], dp[i][num]);
            }
        }
        return res[k];
    }
};
