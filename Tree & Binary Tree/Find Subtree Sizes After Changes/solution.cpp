class Solution {
public:
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> child(n);
        for(int u = 1; u < n; ++u) {
            child[parent[u]].emplace_back(u);
        }
        vector<vector<int>> chars(26);
        function<void(int)> dfs = [&](int u) {
            if(!chars[s[u] - 'a'].empty()) {
                parent[u] = chars[s[u] - 'a'].back();
            }
            chars[s[u] - 'a'].emplace_back(u);
            for(int v: child[u]) {
                dfs(v);
            }
            chars[s[u] - 'a'].pop_back();
        };
        dfs(0);
        vector<vector<int>> after(n);
        for(int u = 1; u < n; ++u) {
            after[parent[u]].emplace_back(u);
        }
        vector<int> result(n);
        function<int(int)> dfs2 = [&](int u) {
            int nodes = 0;
            for(int v: after[u]) {
                nodes += dfs2(v);
            }
            result[u] = nodes + 1;
            return nodes + 1;
        };
        dfs2(0);
        return result;
    }
};
