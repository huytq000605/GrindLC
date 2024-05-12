class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>> result(n-2, vector<int>(n-2));
        for(int i = 1; i < n-1; i++) {
            for(int j = 1; j < n-1; j++) {
                int mx = grid[i][j];
                for(int dr: {-1, 0, 1}) {
                    for(int dc: {-1, 0, 1}) {
                        mx = max(mx, grid[i + dr][j + dc]);
                    }
                }
                result[i-1][j-1] = mx;
            }
        }
        return result;
    }
};
