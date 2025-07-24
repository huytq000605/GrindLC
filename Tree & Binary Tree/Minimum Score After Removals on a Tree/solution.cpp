class Solution {
public:
    int minimumScore(vector<int>& nums, vector<vector<int>>& edges) {
        int xor_all = 0;
        for(int num: nums) xor_all ^= num;
        int n = nums.size();
        vector<vector<int>> tree(n, vector<int>());
        for(auto &edge: edges) {
            int u = edge[0], v = edge[1];
            tree[u].emplace_back(v);
            tree[v].emplace_back(u);
        }
        int result = INT_MAX;
        auto dfs = [&tree, &result, &nums, xor_all](this auto&& dfs, auto u, auto p, auto xor1, bool is_root = false) -> int {
            int xor2 = nums[u];
            for(int v: tree[u]) {
                if(v == p) continue;
                xor2 ^= dfs(v, u, xor1);
            }
            if(xor1 != -1 && !is_root) {
                int xor3 = xor_all ^ xor1 ^ xor2;
                result = min(result, max({xor1, xor2, xor3}) - min({xor1, xor2, xor3}));
            }
            return xor2;
        };

        for(auto &edge: edges) {
            int u = edge[0], v = edge[1];
            if(tree[u].size() > 1) { // then v could be a component
                int xor1 = dfs(v, u, -1);
                dfs(u, v, xor1, true);
            }
            if(tree[v].size() > 1) { // then u could be a component
                int xor1 = dfs(u, v, -1);
                dfs(v, u, xor1, true);
            }
        }
        return result;
    }
};
