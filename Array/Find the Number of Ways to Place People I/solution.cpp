class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), [](auto &p1, auto &p2) -> bool {
            if(p1[0] == p2[0]) {
                return p1[1] > p2[1];
            }
            return p1[0] < p2[0];
        });
        int n = points.size();
        int result = 0;
        for(int i = 0; i < n; ++i) {
            int lower_bound = INT_MIN;
            for(int j = i+1; j < n; ++j) {
                if(points[j][1] > lower_bound && points[j][1] <= points[i][1]) {
                    lower_bound = max(lower_bound, points[j][1]);
                    ++result;
                } 
            }
        }
        return result;
    }
};
