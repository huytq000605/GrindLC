class Solution {
public:
    int largestIsland(vector<vector<int>>& grid) {
        int n = grid.size();
        array<pair<int, int>, 4> ds{{{0,1}, {1,0}, {-1,0}, {0,-1}}};
        vector<int> areas;
        vector<vector<int>> area_idxs(n, vector<int>(n, -1));
        function<void(int, int)> dfs = [&](int r, int c) {
            if(area_idxs[r][c] != -1) return;
            area_idxs[r][c] = areas.size() - 1;
            areas.back() += 1;
            for(auto [dr, dc]: ds) {
                int nr = r + dr, nc = c + dc;
                if(nr < 0 || nr >= n || nc < 0 || nc >= n || !grid[nr][nc]) continue;
                dfs(nr, nc);
            }
        };
        int result{};
        for(int r{}; r < n; ++r) {
            for(int c{}; c < n; ++c) {
                if(grid[r][c]) {
                    areas.emplace_back(0);
                    dfs(r, c);
                    result = max(result, areas.back());
                }
            }
        }
        for(int r{}; r < n; ++r) {
            for(int c{}; c < n; ++c) {
                if(!grid[r][c]) {
                    unordered_set<int> s{};
                    for(auto [dr, dc]: ds) {
                        int nr = r + dr, nc = c + dc;
                        if(nr < 0 || nr >= n || nc < 0 || nc >= n || !grid[nr][nc]) continue;
                        s.emplace(area_idxs[nr][nc]);
                    }
                    
                    int island{1};
                    for(auto a: s) island += areas[a];
                    result = max(result, island);
                }
            }
        }

        return result;
    }
};
