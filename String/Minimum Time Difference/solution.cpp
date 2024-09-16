class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int> times;
        for(auto t: timePoints) {
            int hour = (t[0] - '0') * 10 + t[1] - '0';
            int minute = (t[3] - '0') * 10 + t[4] - '0';
            times.emplace_back(hour * 60 + minute);
        }
        sort(times.begin(), times.end());
        int result = 1440 - (times[times.size() - 1] - times[0]);
        for(int i = 0; i < times.size() - 1; ++i) {
            result = min(result, times[i+1] - times[i]);
        }
        return result;
    }
};
