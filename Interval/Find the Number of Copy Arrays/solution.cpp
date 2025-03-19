class Solution {
public:
    int countArrays(vector<int>& original, vector<vector<int>>& bounds) {
        int n = original.size();
        int result = bounds[0][1] - bounds[0][0] + 1;
        for(int i = 1; i < n; ++i) {
            int d = original[i] - original[i-1];
            bounds[i][0] = max(bounds[i][0], bounds[i-1][0] + d);
            bounds[i][1] = min(bounds[i][1], bounds[i-1][1] + d);
            result = min(result, bounds[i][1] - bounds[i][0] + 1);
        }
        return max(result, 0);
    }
};
