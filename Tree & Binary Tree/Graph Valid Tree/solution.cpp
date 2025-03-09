class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        vector<int> p(n), r(n, 1);
        for(int i{}; i < n ; ++i) p[i] = i;
        function<int(int)> find = [&](int u) {
            if(u != p[u]) p[u] = find(p[u]);
            return p[u];
        };
        auto uni = [&](int u, int v) {
            u = find(u);
            v = find(v);
            if(u == v) return 0;
            if(r[u] < r[v]) swap(u, v);
            r[u] += r[v];
            p[v] = u;
            return 1;
        };
        for(auto &edge: edges) {
            int u = edge[0], v = edge[1];
            if(!uni(u, v)) return false;
        }
        int components{};
        for(int u{}; u < n; ++u) {
            if(u == p[u]) ++components;
        }
        return components == 1;
    }
};
