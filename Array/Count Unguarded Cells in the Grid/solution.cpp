class Solution {
static constexpr array<tuple<int, int, int>, 4> ds{{ {0,1,1}, {1,0,2}, {-1,0,2}, {0,-1,1} }};
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        int result = m*n - guards.size() - walls.size();
        vector<vector<int>> grid(m, vector<int>(n, 0));
        for(auto &g: guards) grid[g[0]][g[1]] = -1;
        for(auto &w: walls) grid[w[0]][w[1]] = -1;
        for(auto &guard: guards) {
            for(auto &[dr, dc, mask]: ds) {
                int r = guard[0] + dr, c = guard[1] + dc;
                // mask is for not going through a cell vertically or horizontally twice
                while(r >= 0 && r < m && c >= 0 && c < n && 
                    grid[r][c] != -1 && (grid[r][c]&mask) == 0) 
                {
                    result -= grid[r][c] == 0;
                    grid[r][c] |= mask;
                    r += dr;
                    c += dc;      
                }
            }
        }
        return result;
    }
};
