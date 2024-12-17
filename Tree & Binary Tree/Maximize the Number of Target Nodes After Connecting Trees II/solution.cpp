class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
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
        
        auto dfs = [&](int u, int p, auto& graph, auto dfs) -> pair<int, int> {
            int even{1}, odd{};
            for(int v: graph[u]) {
                if(v == p) continue;
                auto [e, o] = dfs(v, u, graph, dfs);
                even += o;
                odd += e;
            }
            return {even, odd};
        };
        
        auto [e1, o1] = dfs(0, -1, graph1, dfs);
        auto [e2, o2] = dfs(0, -1, graph2, dfs);
        int additional = max(e2, o2);
        
        vector<int> result(n);
        deque<pair<int, int>> dq{{ {0, -1} }};
        for(int i{}; !dq.empty(); i ^= 1) {
            int l = dq.size();
            for(int j{}; j < l; ++j) {
                auto [u, p] = dq.front();
                dq.pop_front();
                result[u] = (i & 1 ? o1: e1) + additional;
                for(int v: graph1[u]) {
                    if(v == p) continue;
                    dq.emplace_back(v, u);
                }
            }
        }
        
        return result;
        
    }
};
