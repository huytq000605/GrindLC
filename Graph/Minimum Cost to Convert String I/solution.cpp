class Solution {
public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        int n = original.size();
        vector<vector<pair<int, int>>> graph(26, vector<pair<int, int>>());
        for(int i = 0; i < n; i++) {
            auto u = original[i] - 'a';
            auto v = changed[i] - 'a';
            auto w = cost[i];
            graph[u].emplace_back(v, w);
        }

        auto dijkstra = [&](int start) {
            vector<int> distances(26, INT_MAX);
            distances[start] = 0;
            priority_queue<pair<int, int>,
                vector<pair<int, int>>,
                decltype([](auto p1, auto p2) -> bool {
                    return p1.first > p2.first;
                })> pq;
            pq.emplace(0, start);
            while(!pq.empty()) {
                auto [s, u] = pq.top();
                pq.pop();
                for(auto [v, w]: graph[u]) {
                    if(s + w < distances[v]) {
                        distances[v] = s + w;
                        pq.emplace(s+w, v);
                    }
                }
            }
            return distances;
        };

        vector<vector<int>> distances(26, vector<int>());
        for(int i = 0; i < 26; i++) {
            distances[i] = dijkstra(i);
        }
        long long result = 0;
        for(int i = 0; i < source.size(); i++) {
            int cost = distances[source[i] - 'a'][target[i] - 'a'];
            if(cost == INT_MAX) return -1;
            result += cost;
        }
        return result;
    }
};
