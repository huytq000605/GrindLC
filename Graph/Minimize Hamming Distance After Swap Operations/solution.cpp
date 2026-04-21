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
            p[u] = find(p[u]);
        }
        return p[u];
    }
    
    void uni(int u, int v) {
        u = find(u), v = find(v);
        if(u == v) return;
        if(r[u] < r[v]) swap(u, v);
        r[u] += r[v];
        p[v] = u;
    }

};

class Solution {
public:
    int minimumHammingDistance(vector<int>& source, vector<int>& target, vector<vector<int>>& allowedSwaps) {
        int n = source.size();
        auto uf = UF(n);
        for(auto &s: allowedSwaps) {
            uf.uni(s[0], s[1]);
        }
        vector<vector<int>> components(n);
        for(int i = 0; i < n; ++i) {
            components[uf.find(i)].push_back(i);
        }
        int result = 0;
        for(int i = 0; i < n; ++i) {
            if(components[i].empty()) continue;
            unordered_map<int, int> freq;
            for(int i: components[i]) freq[source[i]]++;
            for(int i: components[i]) {
                if(freq.find(target[i]) == freq.end() || !freq[target[i]]) ++result;
                else freq[target[i]]--;
            }
        }
        return result;
    }
};
