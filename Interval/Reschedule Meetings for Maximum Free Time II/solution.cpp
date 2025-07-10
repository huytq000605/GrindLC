class Solution {
public:
    int maxFreeTime(int eventTime, vector<int>& startTime, vector<int>& endTime) {
        vector<pair<int, int>> events;
        int n = startTime.size();
        for(int i{}; i < n; ++i) {
            events.emplace_back(startTime[i], endTime[i]);
        }
        sort(events.begin(), events.end());
        priority_queue<int, vector<int>, greater<int>> pq;
        pq.emplace(events[0].first - 0);
        int max_space{events[0].first - 0};
        for(int i{}; i < n; ++i) {
            auto [s, e] = events[i];
            int space = (i+1<n ? events[i+1].first: eventTime) - e;
            if(space) {
                max_space = max(max_space, space);
                pq.emplace(space);
                while(pq.size() > 3) pq.pop();
            }
        }
        auto valid = [&](int required_space, int left, int right) {
            vector<int> removed;
            bool result{};
            while(!pq.empty()) {
                int s = pq.top(); pq.pop();
                removed.emplace_back(s);                
                if(s < required_space) continue;
                if(s != left && s != right) {
                    result = true;
                    break;
                };
                if(s == left) left = -1;
                else if(s == right) right = -1;
            }
            for(auto s: removed) pq.emplace(s);
            return result;
        };
        int result = max_space;
        for(int i{}, t{}; i < n; ++i) {
            auto [s, e] = events[i];
            int left_space = s - t;
            int right_space = (i+1<n? events[i+1].first: eventTime) - e;
            t = e;
            if(valid(e-s, left_space, right_space)) {
                result = max(result, left_space + right_space + e-s);
            } else {
                result = max(result, left_space + right_space);
            }
        }
        return result;
    }
};
