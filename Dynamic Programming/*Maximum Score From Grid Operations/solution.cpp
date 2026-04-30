class Solution {
public:
    long long maximumScore(vector<vector<int>>& grid) {
        int n = grid.size();
        // dp1[i] = max score if current col has i blacks, exclude its contributions
        // dp2[i] = max score if current col has i blacks, include its contributions
        vector<long long> dp1(n+1), dp2(n+1);
        for(int col = 1; col < n; ++col) {
            vector<long long> ndp1(n+1), ndp2(n+1);
            for(int prev_black = 0; prev_black <= n; ++prev_black) {
                long long cur_val = 0;
                long long prev_val = 0;
                for(int row = 0; row < prev_black; ++row) {
                    cur_val += grid[row][col];
                }
                for(int cur_black = 0; cur_black <= n; ++cur_black) {
                    if(cur_black && cur_black <= prev_black) cur_val -= grid[cur_black-1][col];
                    if(cur_black > prev_black) prev_val += grid[cur_black-1][col-1];
                    int i = cur_black;
                    int j = prev_black;
                    ndp1[i] = max(ndp1[i], max(dp1[j] + prev_val, dp2[j]));
                    ndp2[i] = max(ndp2[i], max(dp2[j] + cur_val, prev_val + cur_val + dp1[j]));
                }
            }
            dp1 = ndp1;
            dp2 = ndp2;
        }
        
        return *max_element(begin(dp2), end(dp2));
    }
};
