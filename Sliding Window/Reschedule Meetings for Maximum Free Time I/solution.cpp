class Solution {
public:
    int maxFreeTime(int eventTime, int k, vector<int>& startTime, vector<int>& endTime) {
        vector<pair<int, int>> events;
        int n = startTime.size();
        for(int i{}; i < n; ++i) {
            events.emplace_back(startTime[i], endTime[i]);
        }
        sort(events.begin(), events.end());
        deque<pair<int, int>> dq;
       
        int result{};
        for(int i{}, t{}, used{}; i < n; ++i) {
            auto [s, e] = events[i];
            dq.emplace_back(s, e);
            used += e - s;
            while(dq.size() > k) {
                auto [s, e] = dq.front();
                t = e;
                used -= e-s;
                dq.pop_front();
            }
            result = max(result, (i+1 < n ? events[i+1].first: eventTime) - t - used);
        }
        return result;
    }
};
