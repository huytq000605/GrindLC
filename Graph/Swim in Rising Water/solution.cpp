class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> p(n*n), r(n*n,1);
        for(int i = 0; i < n*n; ++i) p[i] = i;
        auto find = [&](this auto&& find, int u) -> int {
            if(p[u] != u) {
                p[u] = find(p[u]);
            }
            return p[u];
        };
        auto uni = [&](int u, int v) {
            u = find(u), v = find(v);
            if(u == v) return;
            if(r[u] < r[v]) swap(u, v);
            r[u] += r[v];
            p[v] = u;
        };
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, decltype([](auto &t1, auto &t2) -> bool {
            return get<0>(t1) > get<0>(t2);
        })> pq;
        vector<pair<int, int>> ds{{0,1},{1,0},{-1,0},{0,-1}};
        for(int r = 0; r < n; ++r) {
            for(int c = 0; c < n; ++c) {
                pq.emplace(grid[r][c], r, c);
            }
        }

        while(!pq.empty()) {
            auto [t, r, c] = pq.top(); pq.pop();
            for(auto [dr, dc]: ds) {
                int nr = r + dr, nc = c + dc;
                if(nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
                if(grid[nr][nc] <= t) {
                    uni(r * n + c, nr * n + nc);
                }
            }
            if(find(0) == find(n*n-1)) {
                return t;
            }
        }
        return INT_MAX;
    }
};
