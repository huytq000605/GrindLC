class UF {
public:
    int n;
    vector<int> p, r;
    UF(int _n): n{_n} {
        p.resize(n);
        for(int i = 0; i < n; ++i) p[i] = i;
        r.resize(n, 1);
    }

    int find(int u) {
        if(u != p[u]) p[u] = find(p[u]);
        return p[u];
    }

    int uni(int u, int v) {
        u = find(u);
        v = find(v);
        if(u == v) return 0;
        if(r[u] < r[v]) swap(u, v);
        r[u] += r[v];
        p[v] = u;
        return 1;
    }
};

class Solution {
public:
    int numberOfComponents(vector<vector<int>>& properties, int k) {
        int n = properties.size();
        auto uf = UF(n);
        int result = n;
        vector<unordered_set<int>> ss(n);
        for(int i = 0; i < n; ++i) {
            ss[i] = unordered_set<int>(properties[i].begin(), properties[i].end());
        }
        for(int i = 0; i < n; ++i) {
            for(int j = i+1; j < n; ++j) {
                int common = 0;
                for(int num: ss[i]) {
                    if(ss[j].find(num) != ss[j].end()) {
                        ++common;
                        if(common >= k) {
                            result -= uf.uni(i, j);
                            break;
                        }
                    }
                }
            }
        }
        return result;
    }
};
