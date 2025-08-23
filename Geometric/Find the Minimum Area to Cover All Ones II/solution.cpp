class Solution {
public:
    int minimumSum(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<vector<vector<int>>>> dp(m, vector<vector<vector<int>>>(m, vector<vector<int>>(n, vector<int>(n))));
        auto min_rectangle = [&](int r1, int r2, int c1, int c2) {
            if(dp[r1][r2][c1][c2]) return dp[r1][r2][c1][c2];
            bool have_one = false;
            int max_r = r1, min_r = r2, max_c = c1, min_c = c2;
            for(int r = r1; r <= r2; ++r) {
                for(int c = c1; c <= c2; ++c) {
                    if(grid[r][c]) {
                        max_r = max(max_r, r);
                        min_r = min(min_r, r);
                        max_c = max(max_c, c);
                        min_c = min(min_c, c);
                        have_one = true;
                    }
                }
            }
            // if rectangle doesn't have any one
            if(!have_one) return 1;
            return dp[r1][r2][c1][c2] = (max_r - min_r + 1) * (max_c - min_c + 1);
        };

        auto dfs = [&](this auto&& dfs, int parts, int r1, int r2, int c1, int c2) {
            if(parts == 1) {
                return min_rectangle(r1, r2, c1, c2);
            }
            
            int result = INT_MAX;
            for(int nparts = 1; nparts < parts; nparts++) {
                for(int mr = r1; mr < r2; ++mr) {
                    result = min(result, dfs(nparts, r1, mr, c1, c2) + dfs(parts - nparts, mr+1, r2, c1, c2));
                }
                for(int mc = c1; mc < c2; ++mc) {
                    result = min(result, dfs(nparts, r1, r2, c1, mc) + dfs(parts - nparts, r1, r2, mc+1, c2));
                }
            }
                        cout << parts << " " << r1 << " " << r2 << " " << c1 << " " << c2 << " " << result << endl;

            return result;
        };

        return dfs(3, 0, m-1, 0, n-1);
    }
};
