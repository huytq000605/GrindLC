class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        sort(begin(intervals), end(intervals), [](auto &i1, auto &i2) -> bool {
            if(i1[0] == i2[0]) return i1[1] > i2[1];
            return i1[0] < i2[0];
        });
        int prev = -1;
        int result = 0;
        for(auto& i: intervals) {
            if(i[0] <= prev && i[1] <= prev) continue;
            ++result;
            prev = i[1];
        }
        return result;
    }
};
