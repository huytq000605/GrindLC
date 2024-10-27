class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        // can optimized by using matrix directly instead of creating another
        vector<vector<int>> dp(m+1, vector<int>(n+1));
        int result = 0;
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                if(!matrix[r][c]) continue;
                dp[r+1][c+1] = min({dp[r][c], dp[r][c+1], dp[r+1][c]}) + 1;
                result += dp[r+1][c+1];
            }
        }
        return result;
    }
};
