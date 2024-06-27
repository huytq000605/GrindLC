class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> colors(n, -1);
        auto dfs = [&](int u, int color, auto & dfs_ref) -> bool {
            for(auto v: graph[u]) {
                if(colors[v] != -1) {
                    if(colors[v] != 1 - color) return false;
                    continue;
                }
                colors[v] = 1 - color;
                if(!dfs_ref(v, 1 - color, dfs_ref)) return false;
            }
            return true;
        };
        for(int u = 0; u < n; u++) {
            if(colors[u] == -1) {
                if(!dfs(u, 0, dfs)) return false;
            }
        }
        return true;
    }
};
