class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
        int n = rains.size();
        unordered_map<int, deque<int>> rain_lakes;
        priority_queue<int> need_dry;
        vector<int> result(n, -1);
        for(int i = 0; i < n; ++i) {
            if(rains[i]) {
                rain_lakes[rains[i]].push_back(i);
            }
        }
        for(int i = 0; i < n; ++i) {
            int rain = rains[i];
            if(rain) {
                if(!need_dry.empty() && rains[-need_dry.top()] == rain) return {};
                rain_lakes[rain].pop_front();
                if(!rain_lakes[rain].empty()) {
                    need_dry.push(-rain_lakes[rain].front());
                }
            } else {
                if(need_dry.empty()) result[i] = 1;
                else {
                    result[i] = rains[-need_dry.top()];
                    need_dry.pop();
                }
            }
        }
        return result;
    }
};
