class UF {
    vector<int> p, r;
    public:
    UF(int n) {
        p.resize(n);
        r.resize(n, 1);
        for(int i = 0; i < n; ++i) p[i] = i;
    }
    int find(int u) {
        if(p[u] != u) {
            return find(p[u]);
        }
        return u;
    }

    void uni(int u, int v) {
        u = find(u);
        v = find(v);
        if(u == v) return;
        if(r[u] < r[v]) swap(u, v);
        r[u] += r[v];
        p[v] = u;
    }
};

class Solution {
public:
    vector<bool> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        auto uf = UF(n);
        for(int i = 1; i < n; ++i) {
            if(nums[i] - nums[i-1] <= maxDiff) {
                uf.uni(i, i-1);
            }
        }
        vector<bool> result;
        result.reserve(queries.size());
        for(auto &q: queries) {
            int u = q[0], v = q[1];
            result.push_back(uf.find(u) == uf.find(v));
        }
        return result;
    }
};
