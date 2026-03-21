class Solution {
public:
    vector<vector<int>> reverseSubmatrix(vector<vector<int>>& grid, int x, int y, int k) {
        for(int r = x; r < x+k/2; ++r) {
            for(int c = y;  c < y + k; ++c) { 
                swap(grid[r][c], grid[x+k-1-(r-x)][c]);
            }
        }
        return grid;
    }
};
