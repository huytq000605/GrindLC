class Solution {
public:
    int magnificentSets(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        for(auto &edge: edges) {
            int u = edge[0]-1, v = edge[1]-1;
            graph[u].emplace_back(v);
            graph[v].emplace_back(u);
        }
        
        vector<vector<int>> components;

        function<bool()> is_bipartite = [&]() {
            vector<int> colors(n);

            function<bool(int, int)> dfs = [&](int u, int color) {
                if(colors[u]) return true;
                colors[u] = color;
                components.back().emplace_back(u);
                for(int v: graph[u]) {
                    if(!dfs(v, 3-color) || color == colors[v]) return false;
                }
                return true;
            };
            
            for(int u{}; u < n; ++u) {
                if(!colors[u]) {
                    components.emplace_back();
                    if(!dfs(u, 1)) return false;
                }
            }

            return true;
        };

        if(!is_bipartite()) return -1;
        int result{};
        
        for(auto &component: components) {
            int max_groups{};
            for(int start: component) {
                vector<bool> visited(n);
                int groups{};
                deque<int> dq{start};
                visited[start] = true;
                while(!dq.empty()) {
                    int k = dq.size();
                    ++groups;
                    while(k--) {
                        int u = dq.front(); dq.pop_front();
                        for(int v: graph[u]) {
                            if(visited[v]) continue;
                            dq.emplace_back(v);
                            visited[v] = true;
                        }
                    }
                }
                max_groups = max(max_groups, groups);
            }
            result += max_groups;
        }

        return result;
    }
};
