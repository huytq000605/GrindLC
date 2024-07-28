class Solution {
public:
    int secondMinimum(int n, vector<vector<int>>& edges, int time, int change) {
        priority_queue<pair<int, int>,
            vector<pair<int, int>>,
            decltype([](auto p1, auto p2) {
                return p1.first > p2.first;
            })> pq;
        vector<vector<int>> graph(n, vector<int>());
        for(auto e: edges) {
            auto u = e[0] - 1, v = e[1] - 1;
            graph[u].emplace_back(v);
            graph[v].emplace_back(u);
        }
        vector<pair<int, int>> distances(n, make_pair(INT_MAX, INT_MAX));
        distances[0].first = 0;
        pq.emplace(0, 0);
        bool earliest = true;
        while(!pq.empty()) {
            auto [t, u] = pq.top();
            pq.pop();
            if(u == n-1) {
                if(!earliest) return t;
                earliest = false;
            }
            bool red = (t/change) % 2;
            if(red) t = (t/change + 1) * change;
            for(auto v: graph[u]) {
                if(t + time < distances[v].first) {
                    distances[v].first = t + time;
                    pq.emplace(t + time, v);
                    continue;
                }
                if(t + time > distances[v]. first && t + time < distances[v].second) {
                    distances[v].second = t  + time;
                    pq.emplace(t + time, v);
                }
            }
        }
        return -1;

    }
};
