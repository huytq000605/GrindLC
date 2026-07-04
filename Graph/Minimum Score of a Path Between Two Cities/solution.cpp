class Solution {
public:
    int minScore(int n, vector<vector<int>>& roads) {
        vector<bool> seen(n);
        vector<vector<pair<int, int>>> graph(n);
        for(auto &road: roads) {
            graph[road[0]-1].emplace_back(road[1]-1, road[2]);
            graph[road[1]-1].emplace_back(road[0]-1, road[2]);
        }
        deque<int> dq{0};
        seen[0] = true;
        int result = INT_MAX;
        while(!dq.empty()) {
            auto u = dq.front(); dq.pop_front();
            for(auto [v, w]: graph[u]) {
                result = min(result, w);
                if(!seen[v]) {
                    seen[v] = true;
                    dq.push_back(v);
                }
            }
        }
        return result;
    }
};
