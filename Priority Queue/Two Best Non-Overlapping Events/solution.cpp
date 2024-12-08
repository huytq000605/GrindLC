class Solution {
public:
    int maxTwoEvents(vector<vector<int>>& events) {
        sort(events.begin(), events.end());
        int max_v{};
        int result{};
        priority_queue<pair<int, int>, vector<pair<int, int>>, 
            decltype([](auto &p1, auto &p2) -> bool {
                return p1.first > p2.first;
            })> pq;
        for(auto &event: events) {
            int s = event[0], e = event[1], v = event[2];
            while(!pq.empty() && pq.top().first < s) {
                auto [_, v] = pq.top();
                pq.pop();
                max_v = max(v, max_v);
            }
            result = max(result, v + max_v);
            pq.emplace(e, v);
        }
        return result;
    }
};
