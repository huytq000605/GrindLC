class Solution {
public:
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        vector<int> distances(n, 0);
        vector<int> childs(n, 0);
        vector<vector<int>> graph(n);
        for(auto &edge: edges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        auto dfs = [&](int u, int p) -> pair<int, int> {
            auto dfs_ref = [&](int u, int p, auto &dfs_ref) -> pair<int, int> {
                for(int & v: graph[u]) {
                    if(v == p) continue;
                    auto [ds, ns] = dfs_ref(v, u, dfs_ref);
                    distances[u] += ds + ns;
                    childs[u] += ns;
                }
                return {distances[u], childs[u] + 1};
            };
            return dfs_ref(u, p, dfs_ref);
        };
        
        auto dfs2 = [&](int u, int p) {
            auto dfs_ref = [&](int u, int p, auto &dfs_ref) -> void {
                for(auto & v: graph[u]) {
                    if(v == p) continue;
                    distances[v] += distances[u] - distances[v] - childs[v] + (n - childs[v] - 2);
                    dfs_ref(v, u, dfs_ref);
                }
            };
            dfs_ref(u, p, dfs_ref);
        };

        dfs(0, -1);
        dfs2(0, -1);
        return distances;
    }
};
