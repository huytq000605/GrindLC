class Solution {
public:
    vector<int> zigzagTraversal(vector<vector<int>>& grid) {
        vector<int> result;
        int m = grid.size(), n = grid[0].size();
        for(int i{}; i < m*n; i += 2) {
            int r = i / n, c = i % n;
            if(r & 1) c = n-1-c;
            result.emplace_back(grid[r][c]);
        }
        return result;
    }
};
