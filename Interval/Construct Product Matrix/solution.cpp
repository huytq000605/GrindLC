class Solution {
public:
    vector<vector<int>> constructProductMatrix(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<long> pref(m*n, 1), suff(m*n, 1);
        int MOD = 12345;
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                int i = r * n + c;
                if(i) pref[i] = pref[i-1];
                pref[i] = (pref[i] * grid[r][c]) % MOD;
            }
        }
        for(int r = m-1; r >= 0; --r) {
            for(int c = n-1; c >= 0; --c) {
                int i = r * n + c;
                if(i < m*n-1) suff[i] = suff[i+1];
                suff[i] = (suff[i] * grid[r][c]) % MOD;
                grid[r][c] = (i-1 >= 0 ? pref[i-1]: 1) * (i+1 < m*n ? suff[i+1]: 1) % MOD;
            }
        }
        return grid;
    }
};
