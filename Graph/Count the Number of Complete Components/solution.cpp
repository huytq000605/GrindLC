class UF {
public:
int n;
vector<int> p, r;
    UF(int _n): n{_n} {
        p.resize(n);
        r.resize(n, 1);
        for(int i = 0; i < n; ++i) p[i] = i;
    }

    int find(int u) {
        if(u != p[u]) p[u] = find(p[u]);
        return p[u];
    }

    void uni(int u, int v) {
        u = find(u);
        v = find(v);
        if(u == v) return;
        r[u] += r[v];
        p[v] = u;
    }
};

class Solution {
public:
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        auto uf = UF(n);
        vector<int> degree(n);
        for(auto&e: edges) {
            int u = e[0], v = e[1];
            uf.uni(u, v);
            degree[u]++;
            degree[v]++;
        }
        int components = 0;
        unordered_set<int> non_complete;
        for(int u = 0; u < n; ++u) {
            int p = uf.find(u);
            if(p == u) {
                components++;
            }
            if(degree[u] != uf.r[p] - 1) {
                non_complete.emplace(uf.p[u]);
            }
        }
        return components - non_complete.size();
    }
};
