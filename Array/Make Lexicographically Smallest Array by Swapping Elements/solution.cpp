class UF {
public:
    int n;
    vector<int> p, r;
    vector<vector<int>> values;
    UF(vector<pair<int, int>> &inums) {
        n = inums.size();
        p.resize(n);
        r.resize(n, 1);
        values.resize(n);
        for(int i{}; i < n; ++i) {
            p[i] = i;
            auto [idx, num] = inums[i];
            values[idx].emplace_back(num);
        }
    }

    int find(int u) {
        if(u != p[u]) {
            p[u] = find(p[u]);
        }
        return p[u];
    }

    void un(int u, int v) {
        u = find(u);
        v = find(v);
        if(u == v) return;
        if(r[u] < r[v]) swap(u, v);
        r[u] += r[v];
        p[v] = u;
        for(int val: values[v]) {
            values[u].emplace_back(val);
        }
        values[v].clear();
    }
};

class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        int n = nums.size();
        vector<pair<int, int>> inums;
        for(int i{}; i < n; ++i) {
            inums.emplace_back(i, nums[i]);
        }
        sort(inums.begin(), inums.end(), [](auto &p1, auto &p2) -> bool {
            return p1.second < p2.second;
        });
        auto uf = UF(inums);
        for(int i{}; i < n-1; ++i) {
            if(abs(inums[i].second - inums[i+1].second) <= limit) uf.un(inums[i].first, inums[i+1].first);
        }
        for(int i{}; i < n; ++i) if(uf.find(i) == i) sort(uf.values[i].begin(), uf.values[i].end(), greater<int>());
        vector<int> result;
        for(int i{}; i < n; ++i) {
            auto &vs = uf.values[uf.find(i)];
            result.emplace_back(vs.back());
            vs.pop_back();
        }
        return result;
    }
};
