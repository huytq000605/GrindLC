class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        pair<int, int> ds[4] = {{1,0}, {0,1}, {-1,0}, {0,-1}};
        int result = 0;
        for(int r = 0; r < m; r++) {
            for(int c = 0; c < n; c++) {
                if(grid[r][c] == 1) {
                    int adj = 0;
                    for(auto & d: ds) {
                        int ar = r + d.first, ac = c + d.second;
                        if(ar < 0 || ar >= m || ac < 0 || ac >= n) continue;
                        if(grid[ar][ac]) adj += 1; 
                        
                    }
                    result += 4 - adj;
                }
            } 
        }
        return result;
    }
};
