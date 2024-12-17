class Solution {
public:
    int maxCollectedFruits(vector<vector<int>>& fruits) {
        int n = fruits.size();
        int result{};
        for(int i{}; i < n; ++i) {
            result += fruits[i][i];
            fruits[i][i] = 0;
        }
        vector<int> dp1(n, INT_MIN), dp2(n, INT_MIN);
        dp1[n-1] = fruits[n-1][0];
        dp2[n-1] = fruits[0][n-1];
        for(int i{1}; i < n; i++) {
            // btm left
            vector<int> ndp1(n, INT_MIN), ndp2(n, INT_MIN);
            for(int r{}; r < n; ++r) {
                ndp1[r] = fruits[r][i] + max({r-1 >= 0 ? dp1[r-1] : 0, dp1[r], r+1 < n ? dp1[r+1] : 0});
            }
            swap(dp1, ndp1);
            
            // top right
            for(int c{}; c < n; ++c) {
                ndp2[c] = fruits[i][c] + max({c-1 >= 0? dp2[c-1] : 0, dp2[c], c+1 < n ? dp2[c+1] : 0});
            }
            swap(dp2, ndp2);
        }
        return dp1[n-1] + dp2[n-1] + result;
    }
};
