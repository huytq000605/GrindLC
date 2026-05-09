class Solution {
public:
    vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> result(m, vector<int>(n));
        int layers = min(m, n) / 2;
        for(int layer = 0; layer < layers; ++layer) {
            vector<int> vals;
            // down
            for(int r = layer; r < m - layer; ++r) vals.push_back(grid[r][layer]);
            // right
            for(int c = layer+1; c < n - layer; ++c) vals.push_back(grid[m-1-layer][c]);
            // up
            for(int r = m - 2 - layer; r >= layer; --r) vals.push_back(grid[r][n-1-layer]);
            // left;
            for(int c = n - 2 - layer; c > layer; --c) vals.push_back(grid[layer][c]);

            int sz = vals.size();
            int i = (-(k % sz) + sz) % sz;
            // down
            for(int r = layer; r < m - layer; ++r) result[r][layer] = vals[(i++) % sz];
            // right
            for(int c = layer+1; c < n - layer; ++c) result[m-1-layer][c] = vals[i++ % sz];
            // up
            for(int r = m - 2 - layer; r >= layer; --r) result[r][n-1-layer] = vals[i++ % sz];
            // left;
            for(int c = n - 2 - layer; c > layer; --c) result[layer][c] = vals[i++ % sz];
            
        }
        return result;
    }
};
