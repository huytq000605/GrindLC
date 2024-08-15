class Solution {
public:
    int countGoodNodes(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        vector<vector<int>> tree(n, vector<int>());
        for(auto e: edges) {
            int u = e[0], v = e[1];
            tree[u].emplace_back(v);
            tree[v].emplace_back(u);
        }
        int result = 0;
        auto dfs = [&](int u, int p, auto dfs_ref) -> int {
            int target = -1;
            int n = 1;
            bool good = true;
            for(int v: tree[u]) {
                if(v == p) continue;
                int sz = dfs_ref(v, u, dfs_ref);
                if(target == -1) target = sz;
                if(sz != target) good = false;
                n += sz;
            }
            if(good) result += 1;
            return n;
        };
        dfs(0, -1, dfs);
        return result;
    }
};
