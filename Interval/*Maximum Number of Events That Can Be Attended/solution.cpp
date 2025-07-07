class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        sort(events.begin(), events.end());
        priority_queue<int> pq;
        int e = 0, day = events.front()[0];
        int result = 0;
        for(;e < events.size() || !pq.empty();) {
            while(!pq.empty() && -pq.top() < day) {
                pq.pop();
            }
            while(e < events.size() && events[e][0] == day) {
                pq.emplace(-events[e++][1]);
            }
            if(!pq.empty()) {
                ++result;
                pq.pop();
            }
            day++;
            if(pq.empty() && e < events.size() && events[e][0] > day) day = events[e][0];
        }
        return result;
    }
};
