class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        int result = 1;
        priority_queue<int, vector<int>, greater<int>> ends;
        sort(intervals.begin(), intervals.end(), [](auto &i1, auto &i2) -> bool {
            if(i1[0] == i2[0]) return i1[1] > i2[1];
            return i1[0] < i2[0];
        });
        for(auto &interval: intervals) {
            int start = interval[0], end = interval[1];
            if(!ends.empty() && ends.top() < start) ends.pop();
            ends.emplace(end);
            result = max(result, static_cast<int>(ends.size()));
        }
        return result;
    }
};
