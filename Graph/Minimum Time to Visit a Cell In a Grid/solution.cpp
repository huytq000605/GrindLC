class Solution {
static constexpr array<pair<int, int>, 4> ds{{ {0,1}, {1,0}, {-1,0}, {0,-1} }};
public:
    int minimumTime(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        if(grid[0][1] > 1 && grid[1][0] > 1) return -1;
        vector<vector<int>> ss(m, vector<int>(n, INT_MAX));
        priority_queue<tuple<int, int, int>,
            vector<tuple<int, int, int>>,
            decltype([](auto &t1, auto &t2) -> bool {
                return get<0>(t1) > get<0>(t2);
            })> pq;
        pq.emplace(0, 0, 0);
        while(!pq.empty()) {
            auto [t, r, c] = pq.top();
            if(r == m-1 && c == n-1) return t;
            pq.pop();
            for(auto &[dr, dc]: ds) {
                int nr = r+dr, nc = c+dc;
                if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                int dd = grid[nr][nc] - t;
                int nt = max(grid[nr][nc] + (dd > 0 && dd % 2 == 0), t + 1);
                if(nt >= ss[nr][nc]) continue;
                ss[nr][nc] = nt;
                pq.emplace(nt, nr, nc);
            }
        }
        return -1;
    }
};
