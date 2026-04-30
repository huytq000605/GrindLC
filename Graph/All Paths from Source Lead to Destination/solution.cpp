class Solution {
public:
    bool leadsToDestination(int n, vector<vector<int>>& edges, int source, int destination) {
        vector<vector<int>> graph(n);
        for(auto &e: edges) {
            graph[e[0]].push_back(e[1]);
            if(e[0] == destination) return false;
        }
        vector<int> seen(n);
        auto dfs = [&](this auto& dfs, int u) -> bool {
            if(u == destination) return true;
            if(graph[u].empty()) return false;
            for(auto v: graph[u]) {
                if(seen[v] == 1) return false;
                if(seen[v] == 2) continue;
                seen[v] = 1;
                if(!dfs(v)) return false;
                seen[v] = 2;
            }
            return true;
        };
        seen[source] = 1;
        return dfs(source);
    }
};
