class Solution {
public:
    vector<vector<int>> findFarmland(vector<vector<int>>& land) {
        vector<vector<int>> result;
        int m = land.size(), n = land[0].size();
        for(int r = 0; r < m; r++) {
            for(int c = 0; c < n; c++) {
                if(!land[r][c]) continue;
                int r2 = r, c2 = c;
                while(r2 < m && land[r2][c2]) {
                    r2 += 1;
                }
                r2 -= 1;
                while(c2 < n && land[r2][c2]) {
                    c2 += 1;
                }
                c2 -= 1;
                result.push_back({r, c, r2, c2});
                for(int fr = r; fr <= r2; fr++) {
                    for(int fc = c; fc <= c2; fc++) {
                        land[fr][fc] = 0;
                    }
                }
            }
        }
        return result;
    }
};
