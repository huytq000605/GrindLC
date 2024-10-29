class Solution {
public:
    int maxMoves(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<int> dp(m);
        int result = 0;
        for(int c = 0; c < n-1; ++c) {
            cout << c << endl;
            vector<int> ndp(m);
            for(int r = 0; r < m; ++r) {
                if(c && !dp[r]) continue;
                for(int dr = -1; dr <= 1; ++dr) {
                    int nr = r + dr;
                    if(nr < 0 || nr >= m) continue;
                    if(grid[nr][c+1] <= grid[r][c]) continue;
                    ndp[nr] = max(ndp[nr], dp[r] + 1);
                    result = max(result, ndp[nr]);
                }
            }
            dp = move(ndp);
        }
        
        return result;
    }
};
