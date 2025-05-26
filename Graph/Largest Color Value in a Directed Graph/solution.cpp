class Solution {
public:
    int largestPathValue(string colors, vector<vector<int>>& edges) {
        int n = colors.size();
        vector<vector<int>> graph(n);
        for(auto &e: edges) {
            int u = e[0], v = e[1];
            graph[u].emplace_back(v);
        }
        int result = 0;
        vector<vector<int>> values(n, vector<int>(26));
        vector<int> visited(n);
        auto dfs = [&](this auto& dfs, int u) -> int {
            if(!visited[u]) {
                visited[u] = 1;
                for(int v: graph[u]) {
                    if(dfs(v)) return 1;
                    for(int i = 0; i < 26; ++i) {
                        values[u][i] = max(values[u][i], values[v][i]);   
                    }
                }
                values[u][colors[u] - 'a']++;
                result = max(result, values[u][colors[u] - 'a']);
                visited[u] = 2;
                return 0;
            } else {
                return visited[u] == 1 ? 1: 0;
            }
        };
        for(int u = 0; u < n; ++u) {
            if(dfs(u)) return -1;
        }
        return result;
    }
};
