class Solution {
public:
    pair<int, int> ds[4] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    void dfs(vector<vector<char>>& grid, int& r, int& c) {
        grid[r][c] = '0';
        for(auto & d: ds) {
            int nr = r + d.first, nc = c + d.second;
            if(nr < 0 || nr >= grid.size() || nc < 0 || nc >= grid[0].size()) continue;
            if(grid[nr][nc] == '0') continue;
            dfs(grid, nr, nc);
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int result = 0;
        for(int r = 0; r < grid.size(); r++) {
            for(int c = 0; c < grid[0].size(); c++) {
                if(grid[r][c] == '1') {
                    dfs(grid, r, c);
                    result += 1;
                }
            }
        }
        return result;
    }
};
