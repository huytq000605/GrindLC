class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        std::sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
            return a[0] < b[0];
        });
        int result = 1;
        int mx = points[0][1];
        for(int i = 1; i < points.size(); i++) {
            if(points[i][0] > mx) {
                mx = points[i][1];
                result += 1;
            } else {
                mx = std::min(mx, points[i][1]);
            }
        }
        return result;
    }
};
