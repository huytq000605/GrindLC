class Solution {
public:
    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        vector<vector<long long>> dp(nums1.size() + 1, vector<long long>(nums2.size() + 1, INT_MIN));
        int mn1 = *min_element(begin(nums1), end(nums1));
        int mx1 = *max_element(begin(nums1), end(nums1));
        int mn2 = *min_element(begin(nums2), end(nums2));
        int mx2 = *max_element(begin(nums2), end(nums2));
        if(mn1 > 0 && mx2 < 0) return mn1 * mx2;
        if(mn2 > 0 && mx1 < 0) return mn2 * mx1;
        for(int i = 0; i < nums1.size(); ++i) dp[i][0] = 0;
        for(int i = 0; i < nums2.size(); ++i) dp[0][i] = 0;
        long long result = INT_MIN;
        for(int i = 0; i < nums1.size(); ++i) {
            for(int j = 0; j < nums2.size(); ++j) {
                long long mx = max(dp[i+1][j+1], max(dp[i+1][j], dp[i][j+1]));
                dp[i+1][j+1] = max(mx, dp[i][j] + nums1[i] * nums2[j]);
                result = max(result, dp[i+1][j+1]);
            }
        }
        return result;
    }
};
