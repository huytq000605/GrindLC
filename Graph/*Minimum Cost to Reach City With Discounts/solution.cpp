class Solution {
public:
    int minimumCost(int n, vector<vector<int>>& highways, int discounts) {
        vector<vector<pair<int, int>>> graph(n, vector<pair<int, int>>());
        for(auto way: highways) {
            int u = way[0], v = way[1], c = way[2];
            graph[u].emplace_back(v, c);
            graph[v].emplace_back(u, c);
        }
        priority_queue<tuple<int, int, int>, 
            vector<tuple<int, int, int>>, 
            decltype([](auto p1, auto p2) -> bool {
                return get<0>(p1) > get<0>(p2);
            })> pq;
        pq.emplace(0, 0, discounts);
        vector<int> discount_track(n, -1);
        while(!pq.empty()) {
            // When we reach u the first time, that's the lowest cost we can reach u
            // However we may reach u with higher cost, but with more discounts
            // which can lead to more optimal solution at the end.
            // If we comeback to this node with lte discounts, we skip
            auto [s, u, discount] = pq.top();
            pq.pop();
            if(u == n-1) return s;
            if(discount <= discount_track[u]) continue;
            discount_track[u] = discount;
            for(auto [v, c]: graph[u]) {
                pq.emplace(s + c, v, discount);
                if(discount) {
                    pq.emplace(s + c/2, v, discount - 1);
                }
            }
        }
        return -1;

    }
};
