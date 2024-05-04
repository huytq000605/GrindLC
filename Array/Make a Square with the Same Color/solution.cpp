class Solution {
public:
    bool canMakeSquare(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int ds[2] = {-1, 1};
        for(int dr: ds) {
            for(int dc: ds) {
                int s = (grid[1][1] == 'W') + (grid[1 + dr][1 + dc] == 'W') + (grid[1][1 + dc] == 'W') + (grid[1+dr][1] == 'W');
                if(s == 0 || s == 4 || s == 1 || s == 3) {
                    return true;
                }
            }
            
        }
        return false;
    }
};
