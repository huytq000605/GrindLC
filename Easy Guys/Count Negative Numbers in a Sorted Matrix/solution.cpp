class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int result = 0;
        for(int r = 0, c = grid[0].size(); r < grid.size(); ++r) {
            while(c-1 >= 0 && grid[r][c-1] < 0) --c;
            result += (grid[0].size() - c);
        }
        return result;
    }
};
