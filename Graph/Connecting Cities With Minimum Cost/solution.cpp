class Solution {
public:
    int minimumCost(int n, vector<vector<int>>& connections) {
        sort(connections.begin(), connections.end(), [](auto &c1, auto &c2) -> bool {
            return c1[2] < c2[2];
        });
        vector<int> p(n), r(n, 1);
        for(int i = 0; i < n; ++i) p[i] = i;
        auto find = [&p](this auto&& find, int u) -> int {
            if(u != p[u]) {
                p[u] = find(p[u]);
            }
            return p[u];
        };
        int result = 0;
        for(auto &con: connections) {
            int u = find(con[0]-1), v = find(con[1]-1), w = con[2];
            if(u == v) continue;
            if(r[u] < r[v]) swap(u, v);
            p[v] = u;
            r[u] += r[v];
            result += w;
        }
        if(*max_element(r.begin(), r.end()) != n) return -1;
        return result;
    }
};
