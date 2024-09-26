class NeighborSum {
vector<vector<int>> g;
static constexpr array<pair<int, int>, 4> adjs {{ {0,1}, {1,0}, {0,-1}, {-1, 0} }};
static constexpr array<pair<int, int>, 4> dias {{ {-1, -1}, {-1, 1}, {1, 1}, {1, -1} }};
public:
    NeighborSum(vector<vector<int>>& grid) {
        g = grid;
    }
    
    int adjacentSum(int value) {
        int result = 0;
        for(int r = 0; r < g.size(); r++) {
            for(int c = 0; c < g[0].size(); c++) {
                if(g[r][c] != value) continue;
                for(auto [dr, dc]: adjs) {
                    int nr = r + dr, nc = c + dc;
                    if(nr < 0 || nr >= g.size() || nc < 0 || nc >= g.size()) continue;
                    result += g[nr][nc];
                }
            }
        }
        return result;
    }
    
    int diagonalSum(int value) {
        int result = 0;
        for(int r = 0; r < g.size(); r++) {
            for(int c = 0; c < g[0].size(); c++) {
                if(g[r][c] != value) continue;
                for(auto [dr, dc]: dias) {
                    int nr = r + dr, nc = c + dc;
                    if(nr < 0 || nr >= g.size() || nc < 0 || nc >= g.size()) continue;
                    result += g[nr][nc];
                }
            }
        }
        return result;
    }
};

/**
 * Your NeighborSum object will be instantiated and called as such:
 * NeighborSum* obj = new NeighborSum(grid);
 * int param_1 = obj->adjacentSum(value);
 * int param_2 = obj->diagonalSum(value);
 */
