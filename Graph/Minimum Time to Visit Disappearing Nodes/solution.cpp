class Solution {
public:
    vector<int> minimumTime(int n, vector<vector<int>>& edges, vector<int>& disappear) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        vector<vector<pair<int, int>>> graph(n, vector<pair<int, int>>());
        for(auto & edge: edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            graph[u].emplace_back(w, v);
            graph[v].emplace_back(w, u);
        }
        pq.emplace(0, 0);
        vector<int> result(n, -1);
        result[0] = 0;
        while(pq.size()) {
            auto p = pq.top();
            pq.pop();
            if(p.first > result[p.second]) continue;
            for(auto & e: graph[p.second]) {
                int w = e.first + p.first;
                int v = e.second;
                if(disappear[v] <= w) continue;
                if(result[v] == -1 || w < result[v]) {
                    result[v] = w;
                    pq.emplace(w, v);
                }
            }

        }
        return result;
    }
};
