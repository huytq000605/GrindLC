class Solution {
public:
    vector<int> maxPoints(vector<vector<int>>& grid, vector<int>& queries) {
        vector<pair<int, int>> iqueries;
        for(int i = 0; i < queries.size(); ++i) {
            iqueries.emplace_back(i, queries[i]);
        }
        sort(iqueries.begin(), iqueries.end(), [](auto& p1, auto& p2) {
            return p1.second < p2.second;
        });
        priority_queue<
            tuple<int, int, int>, 
            vector<tuple<int, int, int>>, 
            decltype([](auto& t1, auto& t2) {
                return get<0>(t1) > get<0>(t2);
            })> pq;
        int m = grid.size(), n = grid[0].size();
        
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                pq.emplace(grid[r][c], r, c);
            }
        }
        vector<int> p(m*n);
        for(int i = 0; i < m*n; ++i) p[i] = i;
        vector<int> r(m*n, 1);
        
        auto find = [&](this auto& find, int u) -> int {
            if(u != p[u]) {
                p[u] = find(p[u]);
            }
            return p[u];
        };
        auto uni = [&](int u, int v) {
            u = find(u);
            v = find(v);
            if(u == v) return;
            if(r[u] < r[v]) swap(u, v);
            r[u] += r[v];
            p[v] = u;
        };
        vector<pair<int, int>> ds = {{1,0}, {0,1}, {-1,0}, {0,-1}};
        vector<int> result(queries.size());
        for(auto &[i, q]: iqueries) {
            while(!pq.empty() && get<0>(pq.top()) < q) {
                auto [_, r, c] = pq.top(); pq.pop();
                for(auto [dr, dc]: ds) {
                    int nr = r + dr, nc = c + dc;
                    if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                    if(grid[nr][nc] < q) uni(r*n+c, nr*n+nc);
                }
            }
            result[i] = q > grid[0][0] ? r[find(0)]: 0;
        }
        return result;

    }
};
