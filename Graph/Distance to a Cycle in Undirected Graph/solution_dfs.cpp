class Solution {
public:
    vector<int> distanceToCycle(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        for(auto &edge: edges) {
            int u = edge[0], v = edge[1];
            graph[u].emplace_back(v);
            graph[v].emplace_back(u);
        }
        
        // find the cycle node
        vector<int> seen(n, 0);
        int cycle_node = -1;
        auto dfs = [&](int u, int p, auto dfs) {
            for(auto v: graph[u]) {
                if(v == p) continue;
                if(seen[v] == 1) {
                    cycle_node = u;
                    return true;
                }
                seen[v] = 1;
                if(dfs(v, u, dfs)) return true;
            }
            return false;
        };
        dfs(0, -1, dfs);

        // build the cycle
        for(int i{}; i < n; ++i) seen[i] = 0;
        vector<int> cycle;
        auto dfs2 = [&](int u, int p, auto dfs) {
            cycle.emplace_back(u);
            seen[u] = 1;
            for(auto v: graph[u]) {
                if(v == p) continue;
                if(seen[v]) return true;
                if(dfs(v, u, dfs)) return true;
            }
            seen[u] = 0;
            cycle.pop_back();
            return false;
        };
        dfs2(cycle_node, -1, dfs2);

        // bfs from cycle
        vector<int> result(n, 0);
        deque<pair<int, int>> dq{};
        for(int u: cycle) dq.emplace_back(u, 0);
        while(!dq.empty()) {
            auto [u, s] = dq.front();
            dq.pop_front();
            for(int v: graph[u]) {
                if(seen[v]) continue;
                seen[v] = 1;
                result[v] = s+1;
                dq.emplace_back(v, s+1);
            }
        }
        return result;
    }
};
