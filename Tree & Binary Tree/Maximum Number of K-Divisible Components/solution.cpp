class Solution {
public:
    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {
        vector<vector<int>> tree(n, vector<int>());
        for(auto &edge: edges) {
            int u = edge[0], v = edge[1];
            tree[u].emplace_back(v);
            tree[v].emplace_back(u);
        }
        int result{};
        function<int(int, int)> dfs = [&](int u, int p) -> int {
            int val{values[u]%k};
            for(int v: tree[u]) {
                if(v == p) continue;
                val = (val + dfs(v, u)) % k;
            }
            if(val == 0) ++result;
            return val;
        };
        dfs(0, -1);
        return result;
    }
};
