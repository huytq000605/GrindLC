class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2, int k) {
        int n = edges1.size()+1, m = edges2.size()+1;
        
        auto build_graph = [&](vector<vector<int>>& edges, int n) {
            vector<vector<int>> graph(n);
            for(auto &e: edges) {
                int u = e[0], v = e[1];
                graph[u].emplace_back(v);
                graph[v].emplace_back(u);
            }
            return graph;
        };
        
        vector<vector<int>> graph2 = build_graph(edges2, m);
        vector<vector<int>> graph1 = build_graph(edges1, n);
        
        auto target = [](int u, vector<vector<int>> &graph, int k) {
            if(k < 0) return 0;
            deque<pair<int, int>> dq;
            dq.emplace_back(u, -1);
            int res{1};
            for(int i{}; i < k; ++i) {
                int l = dq.size();
                for(int j{}; j < l; ++j) {
                    auto [u, p] = dq.front();
                    dq.pop_front();
                    for(int v: graph[u]) {
                        if(v == p) continue;
                        dq.emplace_back(v, u);
                    }
                }
                res += dq.size();
            }
            return res;
        };
        
        int additional{};
        for(int u{}; u < m; ++u) additional = max(additional, target(u, graph2, k-1));
        vector<int> result(n, 0);
        for(int u{}; u < n; ++u) result[u] = target(u, graph1, k) + additional; 
        
        return result;
        
    }
};
