class Solution {
public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        vector<vector<pair<int, int>>> tree(n);
        for(auto &edge: edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            tree[u].emplace_back(v, w);
            tree[v].emplace_back(u, w);
        }
        unordered_map<int, int> depths{{nums[0], 1}};
        vector<int> prefix{0};
        pair<int, int> result{0, 1};
        function<void(int, int, int, int)> dfs = [&](int u, int p, int left, int depth) {
            result = min(result, {-(prefix.back()-prefix[left]), depth - left});
            for(auto &[v, w]: tree[u]) {
                if(v == p) continue;
                prefix.emplace_back(prefix.back() + w);
                int prev_depth = depths[nums[v]];
                int new_left = max(left, depths[nums[v]]);
                depths[nums[v]] = depth+1;
                dfs(v, u, new_left, depth + 1);
                depths[nums[v]] = prev_depth;
                prefix.pop_back();
            }
        };
        dfs(0, -1, 0, 1);
        return {-result.first, result.second};
    }
};
