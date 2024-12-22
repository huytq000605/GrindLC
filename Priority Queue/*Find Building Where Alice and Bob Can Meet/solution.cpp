class Solution {
public:
    vector<int> leftmostBuildingQueries(vector<int>& heights, vector<vector<int>>& queries) {
        vector<int> result(queries.size(), -1);
        vector<vector<pair<int, int>>> remaining_queries(heights.size(), vector<pair<int, int>>());
        for(int i{}; i < queries.size(); ++i) {
            auto &query = queries[i];
            auto a = query[0], b = query[1];
            if(a >  b) swap(a, b);
            if(a == b) {
                result[i] = a;
                continue;
            }
            if(heights[b] > heights[a]) {
                result[i] = b;
                continue;
            }
            remaining_queries[b].emplace_back(heights[a], i);
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for(int i{}; i < heights.size(); ++i) {
            while(!pq.empty() && pq.top().first < heights[i]) {
                auto [h, q] = pq.top(); pq.pop();
                result[q] = i;
            }
            for(auto [h, q]: remaining_queries[i]) {
                pq.emplace(h, q);
            }
        }
        return result;
    }
};
