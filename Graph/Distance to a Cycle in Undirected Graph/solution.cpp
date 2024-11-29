class Solution {
public:
    vector<int> distanceToCycle(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        vector<int> degree(n);
        for(auto &edge: edges) {
            int u = edge[0], v = edge[1];
            graph[u].emplace_back(v);
            graph[v].emplace_back(u);
            ++degree[u];
            ++degree[v];
        }

        // bfs from leafs to inside, all the remaining nodes will be cycle
        vector<int> leafs;
        for(int u{}; u < n; ++u) {
            if(degree[u] == 1) leafs.emplace_back(u);
        }
        while(!leafs.empty()) {
            int u = leafs.back();
            leafs.pop_back();
            for(int v: graph[u]) {
                --degree[v];
                if(degree[v] == 1) {
                    leafs.emplace_back(v);
                }
            }
        }

        // bfs from cycle
        vector<int> result(n, INT_MAX);
        deque<pair<int, int>> dq{};
        for(int u{}; u < n; ++u) 
            if(degree[u] > 1) {
                result[u] = 0;
                dq.emplace_back(u, 0);
            }
        
        while(!dq.empty()) {
            auto [u, s] = dq.front();
            dq.pop_front();
            for(int v: graph[u]) {
                if(s+1 < result[v]) {
                    result[v] = s+1;
                    dq.emplace_back(v, s+1);
                }
            }
        }
        return result;
    }
};
