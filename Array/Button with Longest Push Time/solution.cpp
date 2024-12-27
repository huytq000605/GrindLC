class Solution {
public:
    int buttonWithLongestTime(vector<vector<int>>& events) {
        int t0{};
        int result{-1};
        int longest_time{-1};
        
        for(auto &event: events) {
            int i{event[0]}, t{event[1]};
            if(result == -1 || t - t0 > longest_time || (t-t0 == longest_time && i < result)) {
                result = i;
                longest_time = t - t0;
            }
            t0 = t;
        }
        return result;
    }
};
