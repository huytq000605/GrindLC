class UF {
public:
    int n;
    vector<int> r, p;
   
    UF(int _n) {
        n = _n;
        r.resize(n, 1);
        p.resize(n);
        for(int i = 0; i < n; ++i) p[i] = i;
    }

    int find(int u) {
        if(u != p[u]) {
            p[u] = find(p[u]);
        }
        return p[u];
    }

    int uni(int u, int v) {
        u = find(u), v = find(v);
        if(u == v) return 0;
        if(r[u] < r[v]) swap(u, v);
        r[u] += r[v];
        p[v] = u;
        return 1;
    }
};

class Solution {
public:
    int maxStability(int n, vector<vector<int>>& edges, int k) {
        auto uf = UF(n);
        int mi = INT_MAX, lo = 0, hi = 1;
        for(auto &edge: edges) {
            int u = edge[0], v = edge[1], s = edge[2], m = edge[3];
            if(m) {
                if(!uf.uni(u, v)) return -1;
                mi = min(mi, s);
                hi = max(hi, s);
                lo = min(lo, s);
            } else {
                hi = max(hi, s*2);
            } 
        }
        auto valid = [&](UF uf, int k, int res) -> bool {
            for(auto &edge: edges) {
                int u = edge[0], v = edge[1], s = edge[2], m = edge[3];
                if(m) continue;
                if(s >= res) uf.uni(u, v);
            }
            for(auto &edge: edges) {
                int u = edge[0], v = edge[1], s = edge[2], m = edge[3];
                if(m) continue;
                if(s * 2 >= res && k && uf.uni(u, v)) {
                    --k;
                }
            }
            return uf.r[uf.find(0)] == n;
        };

        while(lo < hi) {
            int m = lo + (hi - lo + 1) / 2;
            if(valid(uf, k, m)) {
                lo = m;
            } else {
                hi = m - 1;
            }
        }
        return min(lo, mi) == 0 ? -1: min(lo, mi);
    }
};
