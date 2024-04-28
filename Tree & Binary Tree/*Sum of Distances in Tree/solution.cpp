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

        std::function<pair<int, int>(int, int)> dfs;
        dfs = [&](int u, int p) -> pair<int, int> {
            for(int & v: graph[u]) {
                if(v == p) continue;
                auto [ds, ns] = dfs(v, u);
                distances[u] += ds + ns;
                childs[u] += ns;
            }
            return {distances[u], childs[u] + 1};
        };
        
        std::function<void(int, int)> dfs2;
        dfs2 = [&](int u, int p) {
            for(auto & v: graph[u]) {
                if(v == p) continue;
                distances[v] += distances[u] - distances[v] - childs[v] + (n - childs[v] - 2);
                dfs2(v, u);
            }
        };

        dfs(0, -1);
        dfs2(0, -1);
        return distances;
    }
};
