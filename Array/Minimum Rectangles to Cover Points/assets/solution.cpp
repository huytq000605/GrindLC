class Solution {
public:
    int minRectanglesToCoverPoints(vector<vector<int>>& points, int w) {
        sort(points.begin(), points.end(), [](vector<int> &p1, vector<int> &p2) {
            return p1[0] < p2[0];
        });
        int result = 1;
        int x = points[0][0];
        for(auto & point: points) {
            int px = point[0];
            if(px - x > w) {
                result += 1;
                x = px;
            }
        }
        return result;
    }
};
