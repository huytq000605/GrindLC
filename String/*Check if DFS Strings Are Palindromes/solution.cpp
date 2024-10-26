vector<int> manacher_odd(const string &s) {
    int n = s.size();
    vector<int> m(n, 0);
    int l = 0, r = 0;
    for(int i = 1; i < n; ++i) {
        if(i < r) {
            m[i] = min(r-i, m[l+(r-i)]);
        }
        while(i - m[i] >= 0 && i + m[i] < n && s[i - m[i]] == s[i + m[i]]) {
            ++m[i];
        }
        if(i + m[i] > r) {
            r = i + m[i];
            l = i - m[i];
        }
    }
    return m;
}

class Solution {
public:
    vector<bool> findAnswer(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> child(n);
        for(int u = 1; u < n; ++u) {
            child[parent[u]].emplace_back(u);
        }
        vector<pair<int, int>> ranges(n);
        string ss(n*2+1, '#');
        int i = 1;
        function<void(int)> dfs = [&](int u) {
            int start = i;
            for(int v: child[u]) {
                dfs(v);
            }
            ss[i] = s[u];
            i += 2;
            ranges[u] = {start-1, i-1};
        };
        dfs(0);
        auto m = manacher_odd(ss);

        vector<bool> result(n);
        for(int u = 0; u < n; ++u) {
            auto &[l, r] = ranges[u];
            result[u] = (m[(l+r)/2]-1 >= (r-l+1)/2);
        }
        return result;
    }
};
