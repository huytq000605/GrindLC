class Solution {
public:
    int minCost(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        using tp = tuple<int, int, int, int>;
        vector<tuple<int, int, int>> values;
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                values.emplace_back(grid[r][c], r, c);
            }
        }
        sort(begin(values), end(values));
        vector<int> values_k(k+1);

        priority_queue<tp, vector<tp>, decltype([](auto &t1, auto &t2) -> bool {
            if(get<0>(t1) == get<0>(t2)) {
                return get<3>(t1) < get<3>(t2);
            }
            return get<0>(t1) > get<0>(t2);
        })> pq;
        pq.emplace(0, 0, 0, k);
        vector<vector<vector<int>>> ds(k+1, vector<vector<int>>(m, vector<int>(n, INT_MAX)));
        vector<pair<int, int>> drc{{0, 1}, {1, 0}};
        while(!pq.empty()) {
            auto [s, r, c, l] = pq.top(); pq.pop();
            if(r == m-1 && c == n-1) return s;
            for(auto [dr, dc]: drc) {
                int nr = r + dr, nc = c + dc;
                if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if(s + grid[nr][nc] < ds[l][nr][nc]) {
                    int ns = s + grid[nr][nc];
                    ds[l][nr][nc] = ns;
                    pq.emplace(ns, nr, nc, l);
                };
            }
            if(l) {
                int i = values_k[l];
                for(; i < values.size(); ++i) {
                    auto [v, nr, nc] = values[i]; 
                    if(v > grid[r][c]) break;
                    if(v <= grid[r][c] && s < ds[l-1][nr][nc]) {
                        ds[l-1][nr][nc] = s;
                        pq.emplace(s, nr, nc, l-1);
                    }
                }
                values_k[l] = i;
            }
        }
        return -1;
    }
};
