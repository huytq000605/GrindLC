class Solution {
public:
    int intersectionSizeTwo(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](auto &i1, auto &i2) -> bool {
            if(i1[1] == i2[1]) return i1[0] < i2[0];
            return i1[1] < i2[1];
        });
        int result = 0;
        vector<int> last_two{-1, -1};
        for(int i = 0; i < intervals.size(); ++i) {
            if(intervals[i][0] > last_two[1]) {
                result += 2;
                last_two[1] = intervals[i][1];
                last_two[0] = intervals[i][1]-1;
            } else if(intervals[i][0] > last_two[0]) {
                result += 1;
                last_two[0] = last_two[1];
                last_two[1] = intervals[i][1];
            }
        }
        return result;
    }
};
