class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        // 2 = inprogress
        // -1 = nothing
        vector<int> colors(n, -1);
        function<bool(int)> dfs = [&](int u) -> bool {
            if(colors[u] == 2) return false;
            if(colors[u] != -1) return static_cast<bool>(colors[u]);
            colors[u] = 2;
            for(int v: graph[u]) {
                if(!dfs(v)) {
                    colors[u] = 0;
                    return false;
                }
            }

            colors[u] = 1;
            return true;
        };

        vector<int> result;
        for(int u{}; u < n; ++u) {
            if(dfs(u)) result.emplace_back(u);
        }
        return result;
    }
};
